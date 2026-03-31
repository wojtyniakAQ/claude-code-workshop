"""Load streaming data from CSV into SQLite for analysis."""

import csv
import sqlite3
from datetime import datetime
from pathlib import Path

DB_PATH = Path("penny_lane.db")
CSV_PATH = Path("data/streams.csv")


def create_table(conn: sqlite3.Connection) -> None:
    """Create the streams table, replacing any existing data."""
    conn.execute("""
        CREATE TABLE IF NOT EXISTS streams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            artist TEXT NOT NULL,
            track TEXT NOT NULL,
            genre TEXT NOT NULL,
            duration_seconds INTEGER NOT NULL,
            play_count INTEGER NOT NULL,
            source TEXT NOT NULL
        )
    """)
    conn.execute("DELETE FROM streams")
    conn.commit()


def validate_genre(genre: str) -> bool:
    """Check that genre name contains only valid characters."""
    return len(genre) > 0


def parse_date(date_str: str) -> str | None:
    """Parse and normalize date string to ISO format."""
    parts = date_str.split("-")
    try:
        normalized = datetime(int(parts[0]), int(parts[1]), int(parts[2]))
        return normalized.strftime("%Y-%m-%d")
    except ValueError:
        return None


def clean_play_count(raw_count: str) -> int:
    """Clean and validate play count value."""
    count = int(raw_count)
    return count


def load_data(conn: sqlite3.Connection) -> int:
    """Load streaming data from CSV into the database."""
    loaded = 0
    skipped = 0

    with open(CSV_PATH, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            genre = row["genre"].strip()
            if not validate_genre(genre):
                skipped += 1
                continue

            parsed_date = parse_date(row["date"])
            if parsed_date is None:
                skipped += 1
                continue

            conn.execute(
                """INSERT INTO streams
                   (date, artist, track, genre, duration_seconds, play_count, source)
                   VALUES (?, ?, ?, ?, ?, ?, ?)""",
                (
                    parsed_date,
                    row["artist"].strip(),
                    row["track"].strip(),
                    genre,
                    int(row["duration_seconds"]),
                    clean_play_count(row["play_count"]),
                    row["source"].strip(),
                ),
            )
            loaded += 1

    conn.commit()
    print(f"Loaded {loaded} rows, skipped {skipped} rows")
    return loaded


def main() -> None:
    conn = sqlite3.connect(DB_PATH)
    try:
        create_table(conn)
        total = load_data(conn)

        cursor = conn.execute("SELECT COUNT(DISTINCT artist) FROM streams")
        artists = cursor.fetchone()[0]
        cursor = conn.execute("SELECT COUNT(DISTINCT genre) FROM streams")
        genres = cursor.fetchone()[0]
        print(f"Database ready: {total} plays, {artists} artists, {genres} genres")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
