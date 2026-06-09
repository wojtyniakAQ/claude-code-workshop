"""Tests for scripts/load_streams.py"""

import csv
import sqlite3
import tempfile
from pathlib import Path

import pytest

from load_streams import clean_play_count, create_table, load_data, parse_date, validate_genre


# --- validate_genre ---

def test_validate_genre_simple():
    assert validate_genre("Rock") is True

def test_validate_genre_with_ampersand():
    assert validate_genre("R&B") is True

def test_validate_genre_with_hyphen():
    assert validate_genre("Hip-Hop") is True

def test_validate_genre_empty_string():
    assert validate_genre("") is False

def test_validate_genre_whitespace_only():
    assert validate_genre("   ") is False


# --- parse_date ---

def test_parse_date_valid():
    assert parse_date("2025-01-15") == "2025-01-15"

def test_parse_date_preserves_iso_format():
    assert parse_date("2025-03-07") == "2025-03-07"

def test_parse_date_invalid_month():
    assert parse_date("2025-13-01") is None

def test_parse_date_invalid_day():
    assert parse_date("2025-01-32") is None

def test_parse_date_malformed_too_few_parts():
    assert parse_date("2025-01") is None

def test_parse_date_malformed_not_a_date():
    assert parse_date("notadate") is None


# --- clean_play_count ---

def test_clean_play_count_returns_int():
    assert clean_play_count("273") == 273

def test_clean_play_count_not_decremented():
    assert clean_play_count("1") == 1
    assert clean_play_count("100") == 100

def test_clean_play_count_bad_input_returns_none():
    assert clean_play_count("abc") is None

def test_clean_play_count_empty_returns_none():
    assert clean_play_count("") is None


# --- create_table ---

def test_create_table_creates_streams():
    conn = sqlite3.connect(":memory:")
    create_table(conn)
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    assert ("streams",) in tables
    conn.close()

def test_create_table_clears_existing_data():
    conn = sqlite3.connect(":memory:")
    create_table(conn)
    conn.execute(
        "INSERT INTO streams (date, artist, track, genre, duration_seconds, play_count, source) "
        "VALUES ('2025-01-01', 'A', 'B', 'Rock', 200, 50, 'radio')"
    )
    conn.commit()
    create_table(conn)
    count = conn.execute("SELECT COUNT(*) FROM streams").fetchone()[0]
    assert count == 0
    conn.close()

def test_create_table_column_order():
    conn = sqlite3.connect(":memory:")
    create_table(conn)
    cols = [row[1] for row in conn.execute("PRAGMA table_info(streams)").fetchall()]
    assert cols == ["id", "date", "artist", "track", "genre", "duration_seconds", "play_count", "source"]
    conn.close()


# --- load_data integration ---

@pytest.fixture
def db_with_csv(tmp_path, monkeypatch):
    """Set up an in-memory DB and a temp CSV, patch CSV_PATH, return (conn, csv_path)."""
    import load_streams

    csv_path = tmp_path / "streams.csv"
    rows = [
        ["date", "artist", "track", "genre", "duration_seconds", "play_count", "source"],
        ["2025-01-01", "Disclosure", "Magnets", "Electronic", "411", "273", "playlist"],
        ["2025-01-02", "Robert Glasper", "So Beautiful", "Jazz", "535", "94", "search"],
        ["2025-01-03", "Frank Ocean", "Thinkin Bout You", "R&B", "271", "569", "album"],
    ]
    with open(csv_path, "w", newline="") as f:
        csv.writer(f).writerows(rows)

    monkeypatch.setattr(load_streams, "CSV_PATH", csv_path)

    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    create_table(conn)
    return conn, csv_path


def test_load_data_row_count(db_with_csv):
    conn, _ = db_with_csv
    loaded = load_data(conn)
    assert loaded == 3

def test_load_data_columns_not_swapped(db_with_csv):
    """Catch the column-swap bug: duration_seconds and play_count must go to the right columns."""
    conn, _ = db_with_csv
    load_data(conn)
    row = conn.execute(
        "SELECT duration_seconds, play_count FROM streams WHERE artist='Disclosure'"
    ).fetchone()
    assert row["duration_seconds"] == 411
    assert row["play_count"] == 273

def test_load_data_accepts_genre_with_ampersand(db_with_csv):
    conn, _ = db_with_csv
    load_data(conn)
    row = conn.execute("SELECT genre FROM streams WHERE artist='Frank Ocean'").fetchone()
    assert row["genre"] == "R&B"

def test_load_data_skips_bad_play_count(db_with_csv, tmp_path, monkeypatch):
    import load_streams
    csv_path = tmp_path / "bad.csv"
    rows = [
        ["date", "artist", "track", "genre", "duration_seconds", "play_count", "source"],
        ["2025-01-01", "Artist A", "Track A", "Rock", "200", "abc", "radio"],
        ["2025-01-01", "Artist B", "Track B", "Rock", "200", "50", "radio"],
    ]
    with open(csv_path, "w", newline="") as f:
        csv.writer(f).writerows(rows)
    monkeypatch.setattr(load_streams, "CSV_PATH", csv_path)
    conn = sqlite3.connect(":memory:")
    create_table(conn)
    loaded = load_data(conn)
    assert loaded == 1
