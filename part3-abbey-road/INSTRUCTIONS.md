# Part 3: Abbey Road

**Goal**: You have inherited a broken data pipeline. Fix it, prove it works
with tests, ship it as a PR, and get it reviewed -- all without leaving the
terminal.

---

## Before you start

Make sure `gh` is authenticated:

```bash
gh auth status
```

If not, run `gh auth login` and follow the prompts.

You need your working app from part 1 or 2. Either keep working in that
directory, or copy your app here:

```bash
cp ../part1-penny-lane/app.py .
cp -r ../part1-penny-lane/templates .
cp ../part1-penny-lane/penny_lane.db .
```

---

## Step 1: Fix the Buggy Parser

Someone wrote `scripts/load_streams.py` to import music streaming data into
your database. It runs without crashing -- but the data it loads is wrong.

### Run it

```bash
uv run python scripts/load_streams.py
```

Look at the output. Does anything seem off?

### Verify the data

Run these checks and compare against what you would expect from the raw CSV:

```bash
uv run python -c "
import sqlite3
conn = sqlite3.connect('penny_lane.db')
print('Row count:', conn.execute('SELECT COUNT(*) FROM streams').fetchone()[0])
print('Genres:', [r[0] for r in conn.execute('SELECT DISTINCT genre FROM streams ORDER BY genre')])
print('Sample:', conn.execute('SELECT date, artist, track, play_count, duration_seconds FROM streams LIMIT 3').fetchall())
conn.close()
"
```

**Expected (correct) values:**
- Row count: **1020**
- Genres should include **R&B** (8 genres total)
- Play counts typically range 10--2000; durations typically range 120--900

### Fix it with Claude

There are **4 bugs** in the script. Use Claude Code to find and fix them:

> Read scripts/load_streams.py and data/streams.csv. The script runs but
> loads incorrect data. Compare the loaded data against the raw CSV to find
> bugs. There are 4 of them.

Re-run the script after each fix and verify the data improves.

## Step 2: Write Tests

Now that the parser works, make sure it stays that way. Ask Claude to write
tests that would have caught these bugs:

> Write pytest tests for scripts/load_streams.py. Test that all rows are
> loaded, all genres are preserved (including R&B), dates are parsed
> correctly, and play counts match the source CSV. Use data/streams.csv as
> the test fixture.

Run them and make sure they pass:

```bash
uv run pytest
```

## Step 3: Ship It as a PR

Create a branch, commit the bug fixes and tests, and open a pull request:

> Create a new branch called feat/fix-stream-parser, commit the parser bug
> fixes and tests with a descriptive commit message, and open a pull request
> using gh. The PR should summarize what bugs were found and how the tests
> prevent regressions.

## Step 4: Review the PR

Open a **second terminal** and start a new Claude Code session:

```bash
claude
```

In this fresh session, ask Claude to review the PR you just created:

> Review the open PR on this repo. Read the changes, check for correctness,
> edge cases, and code quality. Leave review comments on anything you would
> flag as a reviewer.

Go back to your first terminal and read the review comments. Address any
feedback Claude left.

This is the real workflow: one Claude writes, another Claude reviews. You
are the decision-maker in between.

---

## Exercise A: Write Your Own Skill

In part 2 you used `/deploy` -- a custom slash command. It's just a
markdown file in `.claude/commands/` that tells Claude what to do. For
example, the deploy skill looks like this:

```
Deploy the app to Google Cloud Run.

Steps:
1. Check if a Procfile exists. If not, create one.
2. Determine a service name from whoami.
3. Run gcloud run deploy ...
```

Now create your own. Pick something useful -- here are some ideas:

- `/seed-data` -- populate the database with test data
- `/check-db` -- verify the database has the right tables and row counts
- `/run-analysis` -- generate a summary report from the streaming data

Tell Claude what you want:

> I want to create a custom slash command called /check-db. When I run it,
> Claude should connect to penny_lane.db, list all tables, and print the
> row count for each one. Create the skill file in .claude/commands/.

Once Claude creates it, test it by typing `/check-db` (or whatever you
named yours) in Claude Code.

## Exercise B: Data Analysis

Use Claude as an analytical tool. Ask it questions about the streaming data:

- "Which genre has the highest average play count?"
- "Is there a correlation between track duration and play count?"
- "Show me the top 5 most-played tracks across all dates"
- "Which month had the most total plays?"

Watch how Claude writes and runs SQL on the fly.

## Bonus: Streaming Analytics Page

If you have time, ask Claude to add an analytics page to your app that
visualizes the streaming data with charts (listening trends, top artists,
genre breakdown). You might find something unexpected in the data.

---

## Reflect

- How did debugging with Claude compare to debugging alone?
- Did having a second Claude review the PR catch anything you missed?
- What would you add to your own projects' CLAUDE.md after this workshop?
