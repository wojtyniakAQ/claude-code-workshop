# Tier 3: Developer Workflows

**Time**: ~20 minutes
**Goal**: Real-world developer workflows -- debugging, data analysis, git
automation, and custom Claude commands.

---

## Before you start

You need your working app from tier 1 or 2. Either keep working in that
directory, or copy your app here:

```bash
cp ../tier1-budget-tracker/app.py .
cp -r ../tier1-budget-tracker/templates .
cp ../tier1-budget-tracker/penny_lane.db .
```

---

## Gate: Fix the Buggy Parser (~8 min)

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

---

## Exercise A: Custom Slash Command (~5 min)

Create a Claude Code command that checks your app's health:

> Create a custom slash command called /healthcheck. It should verify that
> penny_lane.db exists, list all tables, and report the row count in each
> table. Put it in .claude/commands/healthcheck.md.

Test it by typing `/healthcheck` in Claude Code.

## Exercise B: Create a PR (~5 min)

Practice the full git workflow through Claude Code:

> Create a new branch called feat/streaming-data, commit the parser bug
> fixes with a descriptive commit message, and open a pull request using gh.
> The PR should summarize what bugs were found and fixed.

## Exercise C: Data Analysis (~5 min)

Use Claude as an analytical tool. Ask it questions about the streaming data:

- "Which genre has the highest average play count?"
- "Is there a correlation between track duration and play count?"
- "Show me the top 5 most-played tracks across all dates"
- "Which month had the most total plays?"

Watch how Claude writes and runs SQL on the fly.

## Exercise D: Ship It (~5 min)

Deploy your app so anyone can see it:

> Deploy this app to Cloud Run. Use the default project. Make it publicly
> accessible.

If it works, you now have a live URL. Share it with the room.

You just built, debugged, and shipped a web app in 90 minutes -- without
editing a single line of code by hand.

## Bonus: Streaming Analytics Page

If you have time, ask Claude to add an analytics page to your app that
visualizes the streaming data with charts (listening trends, top artists,
genre breakdown). You might find something unexpected in the data.

---

## Reflect

- How did debugging with Claude compare to debugging alone?
- Which exercises felt most useful for your day-to-day work?
- What would you add to your own projects' CLAUDE.md after this workshop?
