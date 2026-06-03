# Leadership Edition -- slide outline

A thin deck. Goal: ~3 minutes up front, then short interludes between builds. Keep
the existing SandboxAQ branding (dark background, amber accent) from
`presentation.pdf`; you can reuse several of those slides as-is (noted below).

This is the source/outline -- turn it into real slides, or have Claude build it as
a single-file HTML deck (eat your own dog food).

---

## INTRO -- before anyone touches the keyboard (~3 min, 3 slides)

### Slide 1 -- Title
> Claude Code -- Leadership Edition
Subtitle: "You talk. It does the work. In your files."

### Slide 2 -- The one promise
- This is not a chatbot you ask questions.
- It's a teammate that works inside your own files and tools.
- Today you'll build real things by describing them in plain English. No coding.

### Slide 3 -- Why not just the chat app? (THE key slide)
Two columns. Keep coming back to this all session.

| Claude chat (file upload) | Claude Code (today) |
|---|---|
| One file at a time | A whole folder of mismatched files at once |
| Writes an answer | Runs real code, and fixes its own mistakes |
| A one-off in a chat bubble | Real files you keep and re-open |
| Re-ask next month from scratch | A reusable button you press again |
| Knows only what you paste | Plugs into your real systems |

Then: "Let's go feel it." -> straight into Segment 0.

---

## INTERLUDE A -- "How it works" (after Segment 1, ~10 min, 5 slides)

Deliver these *after* they've built two things, not before. Reframe the original
deck's developer slides in plain English. (Source slides in parentheses.)

### Slide A1 -- It's a coworker, not a search box (reuse "Let it Code")
- Opinionated. Can't read your mind. Great with clear instructions. Needs the
  occasional reminder. Treat it like a sharp new hire.

### Slide A2 -- It works in YOUR files
- Everything it makes is a real file in your folder that you own.
- Not trapped in a chat. Email it, keep it, open it next year.

### Slide A3 -- House rules: CLAUDE.md (reuse "While My CLAUDE.md Gently Leads")
- A file Claude reads every time -- your standing preferences.
- Set it once ("always use our brand color"), never repeat yourself.
- (Live demo happens here -- see card 02.)

### Slide A4 -- Long chats: /compact (reuse "Getting Better / context")
- Conversations fill up. Type `/compact` and it tidies up and keeps going.
- Important things live in files, so nothing is lost.

### Slide A5 -- You're in control
- It asks before doing anything real. Nothing happens you didn't approve.
- It will not break your laptop.

---

## INTERLUDE B -- Plan mode (inside Segment 3, ~2 min, 1 slide)

### Slide B1 -- Plan before you build (reuse "Hey Claude / use /plan")
- For anything bigger than a quick tweak, plan first.
- Claude proposes the approach; you adjust *before* any work is done.
- Cheap to throw away a plan. Expensive to throw away work.

---

## CLOSE (~1 min, 1 slide)

### Slide C1 -- Where this fits in your week
- Digest a long report. Reconcile messy exports. Prep for a board meeting.
- Prototype an idea to hand to your team.
- Build small re-runnable tools instead of one-off asks.
- It's already on your laptop. Point it at a real (non-secret) folder. Start small.

---

## APPENDIX -- "For Your Engineers" (only if asked)

Keep these from the original deck in your back pocket. Pull them up only if a
technical question comes -- they're not part of the core leadership flow.

- Git: checkouts, merges, conflict resolution
- GitHub: pull requests, comments, code review (one Claude reviews another's work)
- Operations: builds, deployments, configuration; "everything `gcloud` allows"
- Debugging: log analysis, test scripts, root-cause analysis (reuse "Fixing a Hole")
- Worktrees: run risky changes in isolation, in parallel (reuse "Norwegian Worktree")
- Subagents: spin up parallel workers to research/search/explore (reuse "Getting Better")
- One-off scripts: Claude writes, runs, and deletes throwaway code itself
- The 1M-context model for large codebases / long sessions

---

## STRETCH GOALS (to fill 60 -> 90 min)

Each is self-contained; add as time and energy allow.

- **Plug into a real system (~10 min)** -- the strongest "not chat" moment. Show a
  connector / MCP so Claude reaches a live tool instead of an uploaded file (use a
  harmless read-only source given the low-stakes framing). This is the
  enterprise unlock execs remember.
- **Paste a picture (~8 min)** -- screenshot a chart or a competitor's page ->
  "rebuild this" or "what's wrong with this slide?" Big crowd-pleaser.
- **Send it to research (~8 min)** -- "Research [harmless topic], give me a
  one-page brief with sources." Shows fan-out without the jargon.
- **Second app iteration (~10 min)** -- add a new angle, change the story.
- **Marp deep-cut (~8 min)** -- generate a real `.pptx`/PDF for a meeting hand-off.
