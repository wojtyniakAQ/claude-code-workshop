# Workshop: Penny Lane Financial Planner

Work through these tiers in order. Each tier builds on the previous one.
Copy the prompt for each tier into Claude Code and let it build.

**Before each tier**: use `/plan` to enter planning mode, review the plan,
then approve it.

---

## Tier 1: Budget Tracker (~15 min)

Paste this into Claude Code:

> Read PRD.md and CLAUDE.md first. Then build the "Budget tracker" feature
> (section 1 of the PRD). I want to be able to enter my income and expenses,
> have them saved to a database, and see a dashboard with a pie chart of
> spending by category, totals for income/expenses/savings, and a table of
> all expenses. Make it look clean and modern.

Once it's built, run the app:

```bash
uv run uvicorn app:app --reload
```

Open http://localhost:8000 and try adding some expenses.

---

## Tier 2: Savings Projection (~15 min)

> Now build the "Savings projection" feature (section 2 of the PRD). Add a
> new page linked from the navigation. It should show a 12-month line chart
> of cumulative savings based on my current income and expenses. Add sliders
> for income growth rate and expense inflation rate that update the chart in
> real time. Use the data already in the database.

---

## Tier 3: Abbey Road Analytics (~15 min)

> Now build the "Abbey Road Analytics" feature (section 3 of the PRD).
> Import data/streams.csv into a SQLite table. Build an analytics page with:
> monthly listening trends over time (line chart), top 10 artists by play
> count (bar chart), genre breakdown by month (stacked bar chart), and a
> table of viral outlier tracks (those with play counts more than 2 standard
> deviations above their genre average). Use SQL for the analysis, pandas
> only where SQL gets awkward.

---

## Tips

- If something looks wrong, describe the problem to Claude Code and ask it
  to fix it. Don't try to fix code yourself.
- If you want a different layout or color scheme, just ask. ("Make the
  charts use a dark theme", "Put the pie chart next to the table instead of
  above it".)
- If the app crashes, paste the error into Claude Code.
