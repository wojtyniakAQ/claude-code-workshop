"""Generate the deliberately-messy Segment 3 dataset: three exports of the SAME
event signup list, pulled from three different systems (a web form, an email
invite tool, and a calendar RSVP tool).

The same human shows up in more than one file, spelled differently each time
(nickname vs. full name, different domain spellings, different casing). The
job attendees are given is to reconcile the three exports into one clean
attendee list with a defensible headcount.

This replaces the old "three monthly music-streaming exports" dataset.

Required numbers (quoted in the facilitator card and README -- do not drift):
  - webform.csv        : 22 data rows
  - email-invites.csv  : 19 data rows
  - calendar-rsvps.csv : 17 data rows
  - 58 raw rows total -> 41 distinct real people

Canonical dedupe rule (also stated in notes.txt): two rows are the same person
when the email local-part matches after lowercasing and trimming, and the
domain is any of sandboxaq.com, sandboxquantum.com or samdboxaq.com (a
deliberate typo domain). Name spelling is a hint, never the key. Rows whose
email isn't on one of those three domains (or has no usable email at all) are
junk, not people, and never count toward the 41.

The dataset deliberately bakes in all 8 required "mess" types -- see the
comments next to each row group below for which type(s) it demonstrates.

All names are invented; none refer to real people. The three domain spellings
are deliberate and are domains, not people.

Run from the repo root:  python vp-workshop/scripts/make_messy_data.py
"""

import random
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
OUT_DIR = REPO_ROOT / "vp-workshop" / "starter" / "data"

# Only used to shuffle row order within each file so the mess doesn't read as
# hand-sorted by category. The dataset's content (rows, dupes, counts) is
# fully deterministic regardless of shuffle order -- this seed just fixes the
# order so re-running the script byte-for-byte reproduces the same files.
RNG_SEED = 20260901

WEBFORM_HEADER = ["full_name", "email", "team", "submitted_at"]
EMAIL_HEADER = ["Name", "Email Address", "Department", "Responded"]
CALENDAR_HEADER = ["attendee", "mail", "org", "rsvp_date"]

# Each row is a plain 4-tuple matching its file's header, OR the string
# constant below for the one row that's blank except for a stray comma.
BLANK_STRAY_COMMA = "__BLANK_STRAY_COMMA__"

# ---------------------------------------------------------------------------
# webform.csv -- 22 rows (20 real people + 2 junk)
# ---------------------------------------------------------------------------
WEBFORM_ROWS = [
    # Mess #8: appears in all three files, all three spellings different
    # (also demonstrates #1: sandboxquantum.com used for this person in
    # email-invites, and #2: samdboxaq.com used for them in calendar-rsvps).
    ("Isabelle Ng", "isabelle.ng@sandboxaq.com", "Product", "2026-09-01"),
    # Mess #1: domain variant, same person as the sandboxquantum.com row below.
    ("Sofia Reyes", "sofia.reyes@sandboxaq.com", "Design", "2026-08-29"),
    # Mess #2: typo domain -- this is their correct-domain record.
    ("Derek Holloway", "derek.holloway@sandboxaq.com", "Engineering", "2026-08-28"),
    # Mess #3: nickname/full-name pairs (full-name half, x5).
    ("Jennifer Stewart", "jennifer.stewart@sandboxaq.com", "Engineering", "2026-09-02"),
    ("Kathryn Wang", "kathryn.wang@sandboxaq.com", "Product", "2026-09-01"),
    ("Benjamin Torres", "benjamin.torres@sandboxaq.com", "Sales", "2026-08-30"),
    ("Nathaniel Cho", "nathaniel.cho@sandboxaq.com", "Data Science", "2026-09-03"),
    # Plain duplicate people (appear again in another file).
    # Mess #5: leading whitespace in the name.
    (" Marcus Ellison", "marcus.ellison@sandboxaq.com", "Engineering", "2026-08-28"),
    # Mess #4: ALL CAPS email.
    ("Priya Nandakumar", "PRIYA.NANDAKUMAR@SANDBOXAQ.COM", "Support", "2026-09-02"),
    ("Dana Whitfield", "dana.whitfield@sandboxaq.com", "Legal", "2026-08-31"),
    # Single-occurrence real people.
    ("Grace Oyelaran", "grace.oyelaran@sandboxaq.com", "Engineering", "2026-09-01"),
    # Mess #7: missing team.
    ("Hector De La Cruz", "hector.delacruz@sandboxaq.com", "", "2026-08-29"),
    ("Wendy Appiah", "wendy.appiah@sandboxaq.com", "Marketing", "2026-09-04"),
    ("Tobias Lindqvist", "tobias.lindqvist@sandboxaq.com", "", "2026-09-02"),
    ("Mariana Souza", "mariana.souza@sandboxaq.com", "Product", "2026-08-30"),
    ("Felix Okonkwo", "felix.okonkwo@sandboxaq.com", "Data Science", "2026-09-03"),
    ("Ingrid Solberg", "ingrid.solberg@sandboxaq.com", "Finance", "2026-08-28"),
    ("Desmond Clarke", "desmond.clarke@sandboxaq.com", "Engineering", "2026-09-01"),
    ("Nadia Hassan", "nadia.hassan@sandboxaq.com", "People", "2026-08-31"),
    # Mess #5: trailing whitespace in the name.
    ("Corey Blackwood ", "corey.blackwood@sandboxaq.com", "Legal", "2026-09-02"),
    # Mess #6: junk rows -- not people, must not count toward 41.
    ("TEST - DO NOT USE", "test@test.com", "", "2026-01-01"),
    BLANK_STRAY_COMMA,
]

# ---------------------------------------------------------------------------
# email-invites.csv -- 19 rows (all real people, no junk)
# ---------------------------------------------------------------------------
EMAIL_ROWS = [
    # Mess #8 (2nd spelling) + #1 (domain variant) + #4 (ALL CAPS email).
    ("Izzy Ng", "ISABELLE.NG@SANDBOXQUANTUM.COM", "Product", "09/01/2026"),
    # Mess #1: domain variant, same person as the sandboxaq.com row above.
    ("Sofia Reyes", "sofia.reyes@sandboxquantum.com", "Design", "09/03/2026"),
    # Mess #3: nickname halves.
    ("Jenn Stewart", "jennifer.stewart@sandboxaq.com", "Engineering", "09/02/2026"),
    ("Kat Wang", "kathryn.wang@sandboxaq.com", "Product", "09/01/2026"),
    ("Alex Price", "alexandra.price@sandboxaq.com", "Marketing", "09/03/2026"),
    ("Nate Cho", "nathaniel.cho@sandboxaq.com", "Data Science", "09/04/2026"),
    # Plain duplicates (2nd appearance).
    ("Owen Fitzgerald", "owen.fitzgerald@sandboxaq.com", "Finance", "09/02/2026"),
    # Mess #5: leading whitespace in both name and email.
    (" Dana Whitfield", " dana.whitfield@sandboxaq.com", "Legal", "09/03/2026"),
    ("Leo Marchetti", "leo.marchetti@sandboxaq.com", "People", "09/01/2026"),
    # Single-occurrence real people.
    ("Tamsin Okafor", "tamsin.okafor@sandboxaq.com", "Marketing", "09/02/2026"),
    ("Rafael Duarte", "rafael.duarte@sandboxaq.com", "Engineering", "09/04/2026"),
    # Mess #4: ALL CAPS email.
    ("Yuki Tanaka", "YUKI.TANAKA@SANDBOXAQ.COM", "Product", "09/01/2026"),
    # Mess #7: missing department.
    ("Esteban Rios", "esteban.rios@sandboxaq.com", "", "09/03/2026"),
    ("Pauline Vandermeer", "pauline.vandermeer@sandboxaq.com", "", "09/02/2026"),
    ("Dmitri Volkov", "dmitri.volkov@sandboxaq.com", "Data Science", "09/04/2026"),
    ("Chiara Moretti", "chiara.moretti@sandboxaq.com", "Finance", "09/01/2026"),
    ("Samuel Okoye", "samuel.okoye@sandboxaq.com", "Engineering", "09/03/2026"),
    ("Lena Hoffmann", "lena.hoffmann@sandboxaq.com", "People", "09/02/2026"),
    ("Ravi Chandrasekhar", "ravi.chandrasekhar@sandboxaq.com", "Legal", "09/04/2026"),
]

# ---------------------------------------------------------------------------
# calendar-rsvps.csv -- 17 rows (all real people, no junk)
# ---------------------------------------------------------------------------
CALENDAR_ROWS = [
    # Mess #8 (3rd spelling) + #2 (typo domain).
    ("I. Ng", "isabelle.ng@samdboxaq.com", "Product", "1 Sep 2026"),
    # Mess #2: typo domain, at least 2 rows, same person as the sandboxaq.com
    # record in webform.csv.
    ("Derek Holloway", "derek.holloway@samdboxaq.com", "Engineering", "28 Aug 2026"),
    # Mess #5: trailing whitespace in the email.
    ("D. Holloway", "derek.holloway@samdboxaq.com ", "Engineering", "29 Aug 2026"),
    # Mess #3: nickname halves.
    ("Ben Torres", "benjamin.torres@sandboxaq.com", "Sales", "30 Aug 2026"),
    ("Alexandra Price", "alexandra.price@sandboxaq.com", "Marketing", "3 Sep 2026"),
    # Plain duplicates (2nd appearance).
    ("Marcus Ellison", "marcus.ellison@sandboxaq.com", "Engineering", "28 Aug 2026"),
    ("Priya Nandakumar", "priya.nandakumar@sandboxaq.com", "Support", "2 Sep 2026"),
    ("Owen Fitzgerald", "owen.fitzgerald@sandboxaq.com", "Finance", "2 Sep 2026"),
    ("Leo Marchetti", "leo.marchetti@sandboxaq.com", "People", "1 Sep 2026"),
    # Single-occurrence real people.
    ("Abigail Foss", "abigail.foss@sandboxaq.com", "Marketing", "1 Sep 2026"),
    ("Tariq Aziz", "tariq.aziz@sandboxaq.com", "Engineering", "3 Sep 2026"),
    ("Helena Brandt", "helena.brandt@sandboxaq.com", "Product", "30 Aug 2026"),
    ("Kwame Mensah", "kwame.mensah@sandboxaq.com", "Sales", "4 Sep 2026"),
    # Mess #7: missing org.
    ("Fiona Mackenzie", "fiona.mackenzie@sandboxaq.com", "", "2 Sep 2026"),
    ("Omar Saleh", "omar.saleh@sandboxaq.com", "Data Science", "1 Sep 2026"),
    ("Celine Dubois", "celine.dubois@sandboxaq.com", "", "3 Sep 2026"),
    ("Bianca Ferrara", "bianca.ferrara@sandboxaq.com", "People", "4 Sep 2026"),
]

NOTES_TEXT = """Notes from the data team (read me before using these files!)
===========================================================

These three files are exports of the SAME event signup list, pulled from
three different systems (the web sign-up form, the email invite tool, and
the calendar RSVP tool). They do NOT line up cleanly -- the same person
often appears more than once, spelled differently each time. A few things
to know before you reconcile them:

1. COLUMN NAMES AND DATE FORMATS DIFFER BY SYSTEM. webform.csv uses
   full_name/email/team/submitted_at with ISO dates (2026-09-01).
   email-invites.csv uses Name/Email Address/Department/Responded with US
   dates (09/03/2026). calendar-rsvps.csv uses attendee/mail/org/rsvp_date
   with human-written dates (3 Sep 2026). Same underlying fields, different
   dressing.

2. THE CANONICAL DEDUPE RULE: two rows are the same person when the email
   local-part matches after lowercasing and trimming, AND the domain is any
   of sandboxaq.com, sandboxquantum.com, or samdboxaq.com. Treat all three
   domains as the same company. Name spelling is a hint (nicknames, initials,
   typos happen) -- never use it as the matching key.

3. samdboxaq.com IS A TYPO, not a separate company. A few people got invited
   through a system that had this misspelling saved as our domain. Match
   them to their correct-domain record by email local-part as usual.

4. IGNORE JUNK ROWS: at least one obvious test entry (name "TEST - DO NOT
   USE", email test@test.com) and one row that's blank except for a stray
   comma slipped into these exports. Neither is a person -- drop both before
   counting anyone.

5. SOME ROWS ARE MISSING team/department/org. That's a genuinely empty
   field in the source system, not a parsing error -- leave it blank in the
   merged output rather than guessing.

6. WATCH FOR STRAY WHITESPACE AND INCONSISTENT CASING in names and emails
   (leading/trailing spaces, ALL CAPS addresses). Trim and lowercase before
   comparing emails.

Once you've deduped correctly, you should land on 41 distinct real people.
"""


def _write_csv(path: Path, header: list[str], rows: list) -> None:
    lines = [",".join(header)]
    for row in rows:
        if row == BLANK_STRAY_COMMA:
            lines.append(",")
        else:
            lines.append(",".join(row))
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    rng = random.Random(RNG_SEED)

    webform_rows = list(WEBFORM_ROWS)
    email_rows = list(EMAIL_ROWS)
    calendar_rows = list(CALENDAR_ROWS)
    rng.shuffle(webform_rows)
    rng.shuffle(email_rows)
    rng.shuffle(calendar_rows)

    assert len(webform_rows) == 22, f"webform.csv should have 22 rows, got {len(webform_rows)}"
    assert len(email_rows) == 19, f"email-invites.csv should have 19 rows, got {len(email_rows)}"
    assert len(calendar_rows) == 17, f"calendar-rsvps.csv should have 17 rows, got {len(calendar_rows)}"

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    _write_csv(OUT_DIR / "webform.csv", WEBFORM_HEADER, webform_rows)
    _write_csv(OUT_DIR / "email-invites.csv", EMAIL_HEADER, email_rows)
    _write_csv(OUT_DIR / "calendar-rsvps.csv", CALENDAR_HEADER, calendar_rows)
    (OUT_DIR / "notes.txt").write_text(NOTES_TEXT)

    for name in ("webform.csv", "email-invites.csv", "calendar-rsvps.csv", "notes.txt"):
        print(f"wrote {OUT_DIR / name}")


if __name__ == "__main__":
    main()
