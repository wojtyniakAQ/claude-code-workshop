# Tier 1: Follow the Recipe

**Time**: ~15 minutes
**Goal**: Learn Claude Code mechanics by building a working app from a single prompt.

---

## Before you start

```bash
cd tier1-budget-tracker
uv sync
```

## Orientation

Look at the files in this directory:

- **PRD.md** -- what you are building (read it now)
- **CLAUDE.md** -- coding conventions Claude will follow
- **pyproject.toml** -- Python dependencies (already set up)

You will not write any code yourself. Claude Code does all the work.

## Build it

Start Claude Code:

```bash
claude
```

Then paste this prompt:

> Read PRD.md and CLAUDE.md. Build the budget tracker described in the PRD.
> I want to enter my monthly income and add expenses (each with a name,
> amount, and category). Store everything in SQLite. Show a dashboard with a
> pie chart of spending by category, total income, total expenses, net
> savings, and a table of all expenses. Make it clean and modern.

Wait for Claude to finish. It will create `app.py` and HTML templates.

## Run it

```bash
uv run uvicorn app:app --reload
```

Open http://localhost:8000 in your browser.

## Try it

- Set your monthly income
- Add a few expenses with different categories (rent, food, transport, etc.)
- Check that the pie chart, totals, and table all update correctly

## If something is wrong

Describe the problem to Claude Code. Do not edit code yourself. Examples:

- "The pie chart is not showing up"
- "The total expenses are wrong after I delete an entry"
- "I get a 500 error when I add an expense"

## Done?

When you have a working budget tracker, move to **tier2-savings-copilot**.
