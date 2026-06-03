"""Generate the deliberately-messy workshop dataset for Segment 3.

Reads the clean source (part3-abbey-road/data/streams.csv) and splits the first
three months of 2025 into three files that *disagree* with each other the way real
exports from three different systems do:

  - jan.csv : the clean baseline           (ISO dates, original column names)
  - feb.csv : play_count -> plays          (US MM/DD/YYYY dates)
  - mar.csv : date -> day                   (DD-Mon-YYYY dates, first week missing)

A few rows in feb/mar are tagged source=TEST (QA artifacts to be ignored), and
March is missing its first week. notes.txt explains both quirks in plain English.

The mismatches are intentionally MILD (a rename + a date format + a couple of
documented quirks) so Claude reconciles them cleanly on stage, but they are real
enough that a single chat file-upload can't do the job.

Run from the repo root:  python vp-workshop/scripts/make_messy_data.py
"""

import csv
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE = REPO_ROOT / "part3-abbey-road" / "data" / "streams.csv"
OUT_DIR = REPO_ROOT / "vp-workshop" / "starter" / "data"

# Rows whose source is flipped to TEST so the notes.txt "ignore TEST rows" rule
# has something to bite on. Picked deterministically by position within the month.
TEST_ROW_POSITIONS = {2, 11, 20}


def load_rows() -> list[dict]:
    with SOURCE.open(newline="") as fh:
        return list(csv.DictReader(fh))


def rows_for_month(rows: list[dict], month: str) -> list[dict]:
    return [r for r in rows if r["date"].startswith(f"2025-{month}")]


def tag_test_rows(rows: list[dict]) -> list[dict]:
    """Return a copy with a few rows' source set to TEST (deterministic)."""
    out = []
    for i, row in enumerate(rows):
        row = dict(row)
        if i in TEST_ROW_POSITIONS:
            row["source"] = "TEST"
        out.append(row)
    return out


def write_jan(rows: list[dict]) -> None:
    """Clean baseline: ISO dates, original column names."""
    path = OUT_DIR / "jan.csv"
    fields = ["date", "artist", "track", "genre", "duration_seconds", "play_count", "source"]
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row[k] for k in fields})


def write_feb(rows: list[dict]) -> None:
    """play_count -> plays, and US-style MM/DD/YYYY dates. A few TEST rows."""
    path = OUT_DIR / "feb.csv"
    fields = ["date", "artist", "track", "genre", "duration_seconds", "plays", "source"]
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in tag_test_rows(rows):
            iso = datetime.strptime(row["date"], "%Y-%m-%d")
            writer.writerow(
                {
                    "date": iso.strftime("%m/%d/%Y"),
                    "artist": row["artist"],
                    "track": row["track"],
                    "genre": row["genre"],
                    "duration_seconds": row["duration_seconds"],
                    "plays": row["play_count"],
                    "source": row["source"],
                }
            )


def write_mar(rows: list[dict]) -> None:
    """date -> day, DD-Mon-YYYY dates, first week dropped. A few TEST rows."""
    path = OUT_DIR / "mar.csv"
    fields = ["day", "artist", "track", "genre", "duration_seconds", "play_count", "source"]
    kept = [r for r in rows if datetime.strptime(r["date"], "%Y-%m-%d").day > 7]
    with path.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader()
        for row in tag_test_rows(kept):
            iso = datetime.strptime(row["date"], "%Y-%m-%d")
            writer.writerow(
                {
                    "day": iso.strftime("%d-%b-%Y"),
                    "artist": row["artist"],
                    "track": row["track"],
                    "genre": row["genre"],
                    "duration_seconds": row["duration_seconds"],
                    "play_count": row["play_count"],
                    "source": row["source"],
                }
            )


def write_notes() -> None:
    path = OUT_DIR / "notes.txt"
    path.write_text(
        "Notes from the data team (read me before using these files!)\n"
        "===========================================================\n\n"
        "These three files are monthly exports, but they come from three different\n"
        "systems and they do NOT line up cleanly. A couple of things to know:\n\n"
        "1. The column names drift between months. For example one month calls it\n"
        "   'play_count' and another calls it 'plays'; March calls the date column\n"
        "   'day' instead of 'date'. They mean the same thing.\n\n"
        "2. The date formats are all different (2025-02-03 vs 02/03/2025 vs\n"
        "   03-Mar-2025). Same dates, different dressing.\n\n"
        "3. MARCH IS MISSING ITS FIRST WEEK (days 1-7). There was a system\n"
        "   migration, so anything before March 8th just isn't there. That's\n"
        "   expected, not a bug.\n\n"
        "4. IGNORE ANY ROW WHERE source = TEST. Those are QA artifacts from our\n"
        "   testing, not real listens. Leave them out of every total.\n"
    )


def main() -> None:
    rows = load_rows()
    write_jan(rows_for_month(rows, "01"))
    write_feb(rows_for_month(rows, "02"))
    write_mar(rows_for_month(rows, "03"))
    write_notes()
    for name in ("jan.csv", "feb.csv", "mar.csv", "notes.txt"):
        print(f"wrote {OUT_DIR / name}")


if __name__ == "__main__":
    main()
