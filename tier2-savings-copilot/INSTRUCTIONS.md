# Tier 2: Build with Claude as Your Co-pilot

**Time**: ~20 minutes
**Goal**: Work WITH Claude to define requirements, plan, build, and test --
not just paste a prompt.

---

## Before you start

You need your working app from tier 1. Either:

- **Option A**: Keep working in your tier 1 directory. Just read these
  instructions from here.
- **Option B**: Copy your app into this directory:

```bash
cp ../tier1-budget-tracker/app.py .
cp -r ../tier1-budget-tracker/templates .
cp ../tier1-budget-tracker/penny_lane.db .
uv sync
```

## What is different this time

In tier 1 you had a detailed PRD and a ready-made CLAUDE.md. This time you
only have **BRIEF.md** -- a vague product idea. Your job is to work with
Claude to turn that into a real feature.

---

## Step 1: Write a PRD with Claude (~5 min)

Read BRIEF.md yourself first. Then ask Claude to help you flesh it out:

> Read BRIEF.md. Help me turn this into a detailed product requirements
> document. Before writing anything, ask me questions about what I want.

Answer Claude's questions. Let it write PRD.md when you are both aligned.
Review what it produces -- push back if something is off.

## Step 2: Create a CLAUDE.md (~2 min)

Your project has conventions but no CLAUDE.md. Ask Claude to infer one:

> Look at the existing code and create a CLAUDE.md file that documents the
> project conventions, tech stack, and patterns you see.

Review what it writes. Add or remove anything that does not match your
preferences.

## Step 3: Plan before building (~3 min)

Use plan mode to design the approach before writing code:

> /plan

Tell Claude what you want to build (the savings projection). Review the plan.
Is the approach reasonable? Ask it to adjust if needed. Approve the plan when
you are satisfied.

## Step 4: Build the savings projection (~7 min)

Let Claude implement the plan. Watch what it does. If you disagree with a
choice, speak up -- do not wait until the end.

Run the app and test it:

```bash
uv run uvicorn app:app --reload
```

## Step 5: Add tests (~3 min)

Ask Claude to write tests for the calculation logic:

> Write pytest tests for the savings projection calculations. Cover edge
> cases like zero income, negative savings rate, and very high inflation.

Run them:

```bash
uv run pytest
```

If any fail, describe the failures to Claude and iterate.

## Step 6: Build your own feature (remaining time)

Look at BRIEF.md again -- it mentions "one more feature of your choosing."
What would make this app more useful? Tell Claude your idea and build it
together.

Some ideas if you are stuck:
- Recurring expenses (rent, subscriptions) that auto-populate each month
- Expense trends over time (bar chart of spending by month)
- CSV export of all transactions
- Budget limits per category with warnings

## Reflect

Compare this experience to tier 1:
- What was different about collaborating vs. pasting a prompt?
- Did the PRD and planning steps change the quality of the output?
- How did writing tests affect your confidence in the code?

## Done?

When you have a working savings projection and a feature worth pitching,
move to **tier3-dev-workflows**.
