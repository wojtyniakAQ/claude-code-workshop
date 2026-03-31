# Tier 2: Build with Claude as Your Co-pilot

**Time**: ~20 minutes
**Goal**: Work WITH Claude to define requirements, plan, build, and test --
not just paste a prompt.

---

## Before you start

```bash
cd tier2-magical-mystery-setlist
uv sync
```

## What is different this time

In tier 1 you had a detailed PRD and a ready-made CLAUDE.md. This time you
only have **BRIEF.md** -- a vague product idea. Your job is to work with
Claude to turn that into a real app.

---

## Step 1: Write a PRD with Claude (~5 min)

Read BRIEF.md yourself first. Then switch to plan mode (`/plan`) and ask 
Claude to help you flesh it out:

> Read BRIEF.md. Help me turn this into a detailed product requirements
> document. Before writing anything, ask me questions about what I want.

Answer Claude's questions. Let it write PRD.md when you are both aligned.
Review what it produces -- push back if something is off.

## Step 2: Create a CLAUDE.md (~2 min)

This project has no CLAUDE.md. Ask Claude to create one based on
the tech stack and your preferences:

> Create a CLAUDE.md for this project. We are using Python 3.12, FastAPI,
> Jinja2, SQLite (raw sql, no ORM), and Plotly.js via CDN. Keep the app
> in a single file. Add any conventions you think are important.

Review what it writes. Add or remove anything that does not match your
preferences.

## Step 3: Plan before building (~3 min)

Use plan mode to design the approach before writing code:

> /plan

Tell Claude what you want to build. Review the plan. Is the approach
reasonable? Ask it to adjust if needed. Approve the plan when you are
satisfied.

## Step 4: Build it (~7 min)

Let Claude implement the plan. Watch what it does. If you disagree with a
choice, speak up -- do not wait until the end.

Claude should start the server for you. Open http://localhost:8000 and test.

## Step 5: Add tests (~3 min)

Ask Claude to write tests for the core logic:

> Write pytest tests for the setlist logic. Cover edge cases like an empty
> setlist, a set that exceeds the time limit, and reordering songs.

Run them:

```bash
uv run pytest
```

If any fail, describe the failures to Claude and iterate.

## Step 6: Build your own feature (remaining time)

What would make this app more fun or useful? Tell Claude your idea and
build it together.

Some ideas if you are stuck:
- Encore management (separate encore section with its own time budget)
- Song search/filter by genre, tempo, or duration
- Export setlist as a shareable link or printable page
- "Suggest a setlist" that auto-fills based on constraints

## Reflect

Compare this experience to tier 1:
- What was different about collaborating vs. pasting a prompt?
- Did the PRD and planning steps change the quality of the output?
- How did writing tests affect your confidence in the code?

## Done?

When you have a working setlist builder, move to **tier3-dev-workflows**.
