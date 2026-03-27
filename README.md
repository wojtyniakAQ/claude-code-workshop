# Penny Lane Financial Planner -- Claude Code Workshop

A hands-on workshop for learning Claude Code through building a personal
finance application.

## Prerequisites

- Python 3.12+
- Node.js 18+ (for Claude Code)
- A GitHub account (for tier 3 PR exercise)

## Setup

### 1. Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 3. Clone and verify

```bash
git clone <repo-url>
cd claude-code-workshop
cd tier1-budget-tracker && uv sync && cd ..
uv run python -c "import fastapi; print('Ready!')"
```

## Workshop Tiers

Work through the tiers in order. Each builds on the previous one.

| Tier | Directory | Time | What you learn |
|------|-----------|------|----------------|
| 1 | `tier1-budget-tracker/` | ~15 min | Claude Code basics: paste a prompt, get a working app |
| 2 | `tier2-savings-copilot/` | ~20 min | Collaborative workflow: write PRDs, use /plan, add tests |
| 3 | `tier3-dev-workflows/` | ~20 min | Developer workflows: debugging, git, custom commands, data analysis |

Each tier has its own `INSTRUCTIONS.md` with step-by-step guidance. Start
with tier 1.

## Running the app

Once Claude Code builds your app:

```bash
uv run uvicorn app:app --reload
```

Then open http://localhost:8000 in your browser.

## Tips

- Do not edit code yourself. Describe problems to Claude Code and let it fix
  them.
- If the app crashes, paste the error into Claude Code.
- If you want a different look, just ask ("use a dark theme", "make the
  layout two-column").
