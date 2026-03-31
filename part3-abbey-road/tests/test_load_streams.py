"""Tests for load_streams.py parser functions."""

import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from load_streams import clean_play_count, parse_date, validate_genre, create_table, load_data


# ---------------------------------------------------------------------------
# Bug 1: parse_date — month and day were swapped
# ---------------------------------------------------------------------------

class TestParseDate:
    def test_standard_date(self):
        assert parse_date("2025-01-15") == "2025-01-15"

    def test_month_and_day_not_swapped(self):
        # If month/day were swapped, 2025-03-17 would become 2025-17-03 (ValueError → None)
        assert parse_date("2025-03-17") == "2025-03-17"

    def test_preserves_year(self):
        assert parse_date("2025-12-31") == "2025-12-31"

    def test_invalid_date_returns_none(self):
        assert parse_date("2025-13-01") is None

    def test_day_greater_than_12_parses_correctly(self):
        # With the swapped bug, day=20 would be used as month → ValueError → None
        assert parse_date("2025-01-20") == "2025-01-20"


# ---------------------------------------------------------------------------
# Bug 2: clean_play_count — incorrectly subtracted 1 from every count
# ---------------------------------------------------------------------------

class TestCleanPlayCount:
    def test_returns_exact_value(self):
        assert clean_play_count("273") == 273

    def test_no_off_by_one(self):
        # The buggy version returned count - 1
        assert clean_play_count("1") == 1

    def test_large_count(self):
        assert clean_play_count("42434") == 42434

    def test_zero(self):
        assert clean_play_count("0") == 0


# ---------------------------------------------------------------------------
# Bug 3: validate_genre — rejected R&B and Hip-Hop
# ---------------------------------------------------------------------------

class TestValidateGenre:
    def test_simple_genre(self):
        assert validate_genre("Rock") is True

    def test_genre_with_ampersand(self):
        # R&B was incorrectly rejected
        assert validate_genre("R&B") is True

    def test_genre_with_hyphen(self):
        # Hip-Hop was incorrectly rejected
        assert validate_genre("Hip-Hop") is True

    def test_genre_with_space(self):
        assert validate_genre("New Age") is True

    def test_invalid_genre_with_digits(self):
        assert validate_genre("Genre123") is False

    def test_invalid_genre_with_special_chars(self):
        assert validate_genre("R@B") is False


# ---------------------------------------------------------------------------
# Bug 4: load_data — duration_seconds and play_count were swapped in INSERT
# ---------------------------------------------------------------------------

class TestLoadDataColumnOrder:
    def test_duration_and_play_count_not_swapped(self, tmp_path):
        csv_content = (
            "date,artist,track,genre,duration_seconds,play_count,source\n"
            "2025-01-01,Disclosure,Magnets,Electronic,411,273,playlist\n"
        )
        csv_file = tmp_path / "streams.csv"
        csv_file.write_text(csv_content)

        conn = sqlite3.connect(":memory:")
        create_table(conn)

        # Temporarily patch CSV_PATH
        import load_streams as ls
        original = ls.CSV_PATH
        ls.CSV_PATH = csv_file
        try:
            load_data(conn)
        finally:
            ls.CSV_PATH = original

        row = conn.execute(
            "SELECT duration_seconds, play_count FROM streams"
        ).fetchone()
        conn.close()

        duration, play_count = row
        assert duration == 411, f"Expected duration 411, got {duration}"
        assert play_count == 273, f"Expected play_count 273, got {play_count}"

    def test_rb_and_hiphop_rows_are_loaded(self, tmp_path):
        csv_content = (
            "date,artist,track,genre,duration_seconds,play_count,source\n"
            "2025-01-07,Frank Ocean,Thinkin Bout You,R&B,271,569,album\n"
            "2025-01-04,Kendrick Lamar,Money Trees,Hip-Hop,212,164,radio\n"
        )
        csv_file = tmp_path / "streams.csv"
        csv_file.write_text(csv_content)

        conn = sqlite3.connect(":memory:")
        create_table(conn)

        import load_streams as ls
        original = ls.CSV_PATH
        ls.CSV_PATH = csv_file
        try:
            count = load_data(conn)
        finally:
            ls.CSV_PATH = original

        conn.close()
        assert count == 2, f"Expected 2 rows loaded, got {count} (R&B/Hip-Hop rows were likely skipped)"
