"""Tests for scripts/load_streams.py against data/streams.csv."""

import csv
import sqlite3
import sys
from pathlib import Path

import pytest

# Make the scripts directory importable
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
import load_streams

CSV_PATH = Path(__file__).parent.parent / "data" / "streams.csv"


@pytest.fixture(scope="module")
def csv_rows():
    """Raw rows from the CSV, as a list of dicts."""
    with open(CSV_PATH, newline="") as f:
        return list(csv.DictReader(f))


@pytest.fixture(scope="module")
def db(tmp_path_factory):
    """In-memory DB populated by load_data() using the real CSV."""
    db_path = tmp_path_factory.mktemp("db") / "test.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    load_streams.CSV_PATH = CSV_PATH
    load_streams.create_table(conn)
    load_streams.load_data(conn)
    yield conn
    conn.close()


# ---------------------------------------------------------------------------
# Row count
# ---------------------------------------------------------------------------

def test_all_rows_loaded(db, csv_rows):
    """Every row in the CSV must appear in the database — none skipped."""
    count = db.execute("SELECT COUNT(*) FROM streams").fetchone()[0]
    assert count == len(csv_rows)


# ---------------------------------------------------------------------------
# Genre completeness
# ---------------------------------------------------------------------------

def test_all_genres_present(db, csv_rows):
    """Every genre in the CSV, including R&B and Hip-Hop, must be loaded."""
    csv_genres = {row["genre"].strip() for row in csv_rows}
    db_genres = {row[0] for row in db.execute("SELECT DISTINCT genre FROM streams")}
    assert csv_genres == db_genres


def test_rb_rows_loaded(db, csv_rows):
    """R&B rows must not be skipped by genre validation."""
    csv_rb = sum(1 for r in csv_rows if r["genre"].strip() == "R&B")
    db_rb = db.execute(
        "SELECT COUNT(*) FROM streams WHERE genre = 'R&B'"
    ).fetchone()[0]
    assert db_rb == csv_rb


def test_hiphop_rows_loaded(db, csv_rows):
    """Hip-Hop rows must not be skipped by genre validation."""
    csv_hh = sum(1 for r in csv_rows if r["genre"].strip() == "Hip-Hop")
    db_hh = db.execute(
        "SELECT COUNT(*) FROM streams WHERE genre = 'Hip-Hop'"
    ).fetchone()[0]
    assert db_hh == csv_hh


# ---------------------------------------------------------------------------
# Date parsing
# ---------------------------------------------------------------------------

def test_dates_are_iso_format(db):
    """All stored dates must be valid YYYY-MM-DD strings."""
    rows = db.execute("SELECT DISTINCT date FROM streams").fetchall()
    for (date_str,) in rows:
        parts = date_str.split("-")
        assert len(parts) == 3, f"Bad date format: {date_str}"
        year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
        assert 2020 <= year <= 2030, f"Unexpected year in {date_str}"
        assert 1 <= month <= 12, f"Month out of range in {date_str}"
        assert 1 <= day <= 31, f"Day out of range in {date_str}"


def test_dates_not_swapped(db):
    """Dates must preserve the original month and day (not swapped)."""
    # The CSV has 2025-01-15; if month/day were swapped this becomes 2025-05-01
    # and all dates with day > 12 would be dropped.  Verify a late-month date survives.
    count = db.execute(
        "SELECT COUNT(*) FROM streams WHERE date LIKE '%-15' OR date LIKE '%-16'"
        " OR date LIKE '%-17' OR date LIKE '%-18' OR date LIKE '%-19'"
        " OR date LIKE '%-20' OR date LIKE '%-21' OR date LIKE '%-22'"
        " OR date LIKE '%-23' OR date LIKE '%-24' OR date LIKE '%-25'"
        " OR date LIKE '%-26' OR date LIKE '%-27' OR date LIKE '%-28'"
        " OR date LIKE '%-29' OR date LIKE '%-30' OR date LIKE '%-31'"
    ).fetchone()[0]
    assert count > 0, "No dates with day >= 15 found — month/day may be swapped"


def test_specific_date_preserved(db):
    """Spot-check: 2025-01-15 in CSV must be stored as 2025-01-15, not 2025-05-01."""
    count = db.execute(
        "SELECT COUNT(*) FROM streams WHERE date = '2025-01-15'"
    ).fetchone()[0]
    assert count > 0


# ---------------------------------------------------------------------------
# Play counts
# ---------------------------------------------------------------------------

def test_play_counts_match_csv(db, csv_rows):
    """Total play count summed across all rows must equal the CSV sum exactly."""
    csv_total = sum(int(r["play_count"]) for r in csv_rows)
    db_total = db.execute("SELECT SUM(play_count) FROM streams").fetchone()[0]
    assert db_total == csv_total


def test_play_counts_not_off_by_one(db, csv_rows):
    """Individual play counts must not be decremented (no spurious -1 adjustment)."""
    # Spot-check the first row: Disclosure Magnets 2025-01-01, play_count=273
    first = csv_rows[0]
    row = db.execute(
        "SELECT play_count FROM streams WHERE date=? AND artist=? AND track=?",
        (first["date"], first["artist"].strip(), first["track"].strip()),
    ).fetchone()
    assert row is not None
    assert row[0] == int(first["play_count"])


# ---------------------------------------------------------------------------
# Column assignment (duration_seconds vs play_count not swapped)
# ---------------------------------------------------------------------------

def test_duration_seconds_not_swapped(db, csv_rows):
    """duration_seconds in the DB must match the CSV column, not play_count."""
    # duration_seconds values in the CSV are in the hundreds (song lengths in seconds).
    # play_count values can be in the thousands.  If columns are swapped, many
    # duration_seconds values would be implausibly large (>10 000).
    row = db.execute(
        "SELECT MAX(duration_seconds) FROM streams"
    ).fetchone()[0]
    assert row < 2000, (
        f"Max duration_seconds={row} is implausibly large — columns may be swapped"
    )


def test_play_count_column_not_swapped(db, csv_rows):
    """play_count in the DB must not contain duration_seconds values."""
    # If swapped, play_count would hold durations (< ~1000 seconds).
    # The CSV has play counts well above 1000 for popular tracks.
    high_play_count = db.execute(
        "SELECT COUNT(*) FROM streams WHERE play_count > 1000"
    ).fetchone()[0]
    csv_high = sum(1 for r in csv_rows if int(r["play_count"]) > 1000)
    assert high_play_count == csv_high


def test_spot_check_duration_and_play_count(db, csv_rows):
    """Spot-check one row's duration_seconds and play_count against the CSV."""
    first = csv_rows[0]  # Disclosure, Magnets, 2025-01-01, duration=411, plays=273
    row = db.execute(
        "SELECT duration_seconds, play_count FROM streams"
        " WHERE date=? AND artist=? AND track=?",
        (first["date"], first["artist"].strip(), first["track"].strip()),
    ).fetchone()
    assert row is not None
    assert row[0] == int(first["duration_seconds"])
    assert row[1] == int(first["play_count"])
