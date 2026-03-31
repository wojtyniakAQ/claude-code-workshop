"""Regression tests for the four bugs found in scripts/load_streams.py."""

import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from load_streams import clean_play_count, parse_date, validate_genre, create_table, load_data


# ── Bug 1: parse_date swapped month and day ────────────────────────────────

class TestParseDate:
    def test_standard_date_parses_correctly(self):
        assert parse_date("2025-01-15") == "2025-01-15"

    def test_month_is_not_swapped_with_day(self):
        # Before the fix, datetime(2025, day=3, month=1) → "2025-03-01"
        result = parse_date("2025-01-03")
        assert result == "2025-01-03", f"Got {result} — month and day may be swapped"

    def test_day_greater_than_12_does_not_get_skipped(self):
        # Before the fix, day=13 was used as month → ValueError → returned None
        assert parse_date("2025-01-13") == "2025-01-13"
        assert parse_date("2025-03-31") == "2025-03-31"

    def test_invalid_date_returns_none(self):
        assert parse_date("2025-13-01") is None
        assert parse_date("not-a-date") is None

    def test_end_of_month_dates(self):
        assert parse_date("2025-12-31") == "2025-12-31"
        assert parse_date("2025-02-28") == "2025-02-28"


# ── Bug 2: validate_genre rejected R&B and Hip-Hop ────────────────────────

class TestValidateGenre:
    def test_plain_genres_are_valid(self):
        for genre in ("Rock", "Pop", "Jazz", "Classical", "Electronic", "Indie"):
            assert validate_genre(genre), f"{genre} should be valid"

    def test_ampersand_genre_is_valid(self):
        # Before the fix, "R&B" failed isalpha() → entire genre was skipped
        assert validate_genre("R&B"), "R&B should be a valid genre"

    def test_hyphenated_genre_is_valid(self):
        # Before the fix, "Hip-Hop" failed isalpha() → entire genre was skipped
        assert validate_genre("Hip-Hop"), "Hip-Hop should be a valid genre"

    def test_genre_with_spaces_is_valid(self):
        assert validate_genre("New Wave"), "Genres with spaces should be valid"

    def test_truly_invalid_genre_is_rejected(self):
        assert not validate_genre("123")
        assert not validate_genre("!!!")


# ── Bug 3: clean_play_count incorrectly subtracted 1 ─────────────────────

class TestCleanPlayCount:
    def test_play_count_is_not_decremented(self):
        # Before the fix, every count was off by -1
        assert clean_play_count("100") == 100
        assert clean_play_count("273") == 273
        assert clean_play_count("1") == 1

    def test_large_play_count_is_preserved(self):
        assert clean_play_count("9999") == 9999


# ── Bug 4: duration_seconds and play_count were swapped in INSERT ─────────

class TestColumnOrder:
    def _make_db(self, tmp_path):
        """Create an in-memory DB, seed one row, return the loaded row."""
        csv_content = (
            "date,artist,track,genre,duration_seconds,play_count,source\n"
            "2025-01-01,Disclosure,Magnets,Electronic,411,273,playlist\n"
        )
        csv_file = tmp_path / "test_streams.csv"
        csv_file.write_text(csv_content)

        import scripts.load_streams as loader
        original_csv = loader.CSV_PATH
        original_db = loader.DB_PATH
        try:
            loader.CSV_PATH = csv_file
            conn = sqlite3.connect(":memory:")
            conn.row_factory = sqlite3.Row
            create_table(conn)
            load_data(conn)
            row = conn.execute("SELECT * FROM streams").fetchone()
            return dict(row)
        finally:
            loader.CSV_PATH = original_csv
            loader.DB_PATH = original_db

    def test_duration_seconds_stored_correctly(self, tmp_path):
        row = self._make_db(tmp_path)
        assert row["duration_seconds"] == 411, (
            f"Expected duration_seconds=411, got {row['duration_seconds']} "
            "(may be swapped with play_count)"
        )

    def test_play_count_stored_correctly(self, tmp_path):
        row = self._make_db(tmp_path)
        assert row["play_count"] == 273, (
            f"Expected play_count=273, got {row['play_count']} "
            "(may be swapped with duration_seconds)"
        )
