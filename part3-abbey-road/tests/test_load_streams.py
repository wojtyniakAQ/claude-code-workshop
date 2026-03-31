"""Tests for scripts/load_streams.py"""

import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from load_streams import clean_play_count, create_table, parse_date, validate_genre


# --- validate_genre ---

def test_validate_genre_simple():
    assert validate_genre("Rock") is True

def test_validate_genre_with_ampersand():
    assert validate_genre("R&B") is True

def test_validate_genre_with_hyphen():
    assert validate_genre("Hip-Hop") is True

def test_validate_genre_empty_string():
    assert validate_genre("") is False


# --- parse_date ---

def test_parse_date_valid():
    assert parse_date("2025-01-15") == "2025-01-15"

def test_parse_date_preserves_iso_format():
    result = parse_date("2025-03-07")
    assert result == "2025-03-07"

def test_parse_date_invalid_month():
    assert parse_date("2025-13-01") is None

def test_parse_date_invalid_day():
    assert parse_date("2025-01-32") is None


# --- clean_play_count ---

def test_clean_play_count_returns_int():
    assert clean_play_count("273") == 273

def test_clean_play_count_not_decremented():
    # Ensure play count is not off-by-one
    assert clean_play_count("1") == 1
    assert clean_play_count("100") == 100


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
