# Penny Lane Financial Planner -- Product Requirements

## Vision

A simple, interactive personal finance tool that helps users understand their
spending, project their savings, and explore music streaming data.

## Users

Anyone who wants a quick picture of their financial health. No finance
background required.

## Core features

### 1. Budget tracker

- User enters their monthly income
- User adds expenses, each with a name, amount, and category
- The app stores all entries in a database
- A dashboard shows:
  - A pie chart of spending by category
  - Total income, total expenses, and net savings
  - A table of all entered expenses

### 2. Savings projection

- A projection page that shows a 12-month savings forecast
- A line chart of cumulative savings over time
- Interactive sliders for:
  - Monthly income growth rate (0--10%)
  - Monthly expense inflation rate (0--10%)
- The chart updates in real time as sliders move

### 3. Abbey Road Analytics

- Import the provided CSV of ~1,000 music streaming plays
- An analytics dashboard showing:
  - Monthly listening trends: total plays over time (line chart)
  - Top 10 artists by total play count (bar chart)
  - Genre breakdown by month (stacked bar chart)
  - Viral outliers: flag tracks with play counts more than 2 standard
    deviations above their genre average
- All analysis is done via SQL queries against the imported data in SQLite

## Non-goals

- User authentication
- Multi-user support
- Real bank integrations
- Mobile-specific design
