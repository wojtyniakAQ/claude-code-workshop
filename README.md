# All You Need is Claude -- Claude Code Workshop

A hands-on workshop for learning Claude Code through building web
applications.

## Setup

If you followed the prep guide, you already have everything you need
(`uv`, `gh`, Claude Code). Just clone and verify:

```bash
git clone https://github.com/wojtyniakAQ/claude-code-workshop
cd claude-code-workshop/part1-penny-lane
uv sync
uv run python -c "import fastapi; print('Ready!')"
```

## Workshop Parts

Work through the parts in order.

| Part | Directory | What you learn |
|------|-----------|----------------|
| 1 | `part1-penny-lane/` | Claude Code basics: paste a prompt, get a working app |
| 2 | `part2-magical-mystery-tour/` | Collaborative workflow: write PRDs, use /plan, add tests, deploy |
| 3 | `part3-abbey-road/` | Developer workflows: debugging, git, custom commands, data analysis |

Each part has its own `INSTRUCTIONS.md` with step-by-step guidance. Start
with part 1.

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

## Facilitator notes

- **Show and tell after part 1**: Ask 1-2 people to share their screen.
  Dashboards will look different based on prompting style -- point that out.
- **Float during exercises**: Circulate and help people who are stuck,
  especially non-technical participants. Nudge on prompt phrasing.
- **Bug hunt debrief in part 3**: After the parser exercise, quick show of
  hands -- "Who found all 4 bugs?" Discuss the ones people missed.
