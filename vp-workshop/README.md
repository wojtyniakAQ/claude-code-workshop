# Claude Code Workshop -- Leadership Edition

A 60-minute (stretch: 90) hands-on session for non-technical executives. By the
end, every participant has personally built a working app, turned a folder of
messy data into something useful, made a reusable tool, and produced a shareable
deck -- without ever opening a terminal or touching code.

This is the **leadership edition**. The engineer edition (the `part1`/`part2`/
`part3` folders) is a different, code-heavy track; don't mix them.

## The one idea the whole session is built around

A VP can already drop a spreadsheet into the Claude chat app and get a chart back.
So the question this workshop has to answer is: **why do I need Claude *Code*?**

Every segment is chosen to show what only Claude Code does. Say this out loud
early, and keep pointing back to it:

| Claude chat (file upload) | Claude Code (what we show) |
|---|---|
| One file at a time | A whole folder of mismatched files at once |
| Writes an answer | Runs real code, and fixes its own mistakes by re-checking |
| A one-off artifact in a chat bubble | Real files in your folder you keep and re-open |
| You re-ask next month from scratch | A reusable button (`/command`) you press again |
| Knows only what you paste | Plugs into your real systems via connectors |

"Drop a file, get a report" is the baseline we are beating, not the demo.

## Format: build first, explain later

Don't lecture for 15 minutes up front. Let them feel the magic in the first five
minutes, then explain. The deck is trimmed to a ~3-minute intro plus two short
just-in-time interludes (see `presentation-vp/outline.md`).

## Run of show (60-minute core)

| # | Segment | Min | Card |
|---|---|---|---|
| 0 | Say hello (open an empty folder, one delightful prompt) | 6 | `cards/00-say-hello.md` |
| - | Thin intro (3 slides: what it is, the promise, the chat-vs-Code table) | 3 | `presentation-vp/outline.md` |
| 1 | Your first build (meeting-cost calculator, iterate by talking) | 13 | `cards/01-first-build.md` |
| 2 | How it works (coworker, your files, teaching preferences, staying on track, control) | 10 | `cards/02-how-it-works.md` |
| 3 | The real difference (fetch the messy data -> runs code -> interactive app -> reusable button) | 20 | `cards/03-real-difference.md` |
| 4 | Share it (regenerate the work as an HTML deck) | 6 | `cards/04-share-it.md` |
| - | Wrap (where this fits in their week) | 2 | -- |

Stretch goals to fill 60 -> 90 min are at the bottom of `presentation-vp/outline.md`.

## What participants open

Do **not** ask non-technical execs to clone a git repo. Each participant just
opens a brand-new **empty folder** in the desktop app (Code tab -> Select folder ->
make a new folder). That's the whole setup -- nothing to download up front.

The only download happens later, in **Segment 3**, and only when it's needed:
Claude fetches the messy dataset (`jan.csv`, `feb.csv`, `mar.csv`, `notes.txt`)
straight from the public repo into a `data/` folder (the paste prompt is in
`cards/03-real-difference.md`). Segments 0-2 need no files -- those build prompts
are self-contained.

No house-rules / `CLAUDE.md` file to manage: every build prompt already asks for
"a single self-contained HTML file... show it to me," so the preview-pane behavior
is baked into the prompts. (The Segment 2 "teach a preference" demo works by
*asking* Claude to remember something; it saves to its own memory, not a file the
VP ever has to see.)

Everything in `vp-workshop/` (this README, `cards/`, `presentation-vp/`,
`scripts/`, `starter/`) is for you, the facilitator. Participants don't need it.

## Getting the data onto each laptop (no git)

**Primary path -- let Claude fetch it.** In Segment 3 the card's paste prompt
points Claude at the public raw URLs and it downloads the four data files. One
paste, deterministic, no account, nothing to hunt for. Requirements:
`vp-workshop/` must be on `main` (URLs are
`https://raw.githubusercontent.com/wojtyniakAQ/claude-code-workshop/main/vp-workshop/starter/data/...`)
and the room must reach github.com. Verify both in your dry-run.

**Fallback path -- a zip (offline-proof).** If the room's wifi or a firewall might
block GitHub, email/Slack the data ahead of time -- no account needed. A prebuilt
**`vp-workshop/data.zip`** is included (it unzips to a `data/` folder). If you
change the dataset, regenerate it:

```bash
cd vp-workshop/starter && zip -r ../data.zip data -x '*.DS_Store'
```

If you go the zip route, at Segment 3 tell participants: "skip the download prompt
-- unzip today's `data` folder into your workshop folder instead," then continue
from the explore step.

## The Segment 3 dataset

Three monthly exports that disagree the way real systems do: renamed columns
(`play_count` vs `plays`, `date` vs `day`), three different date formats, March
missing its first week, and a few `source=TEST` junk rows the notes say to ignore.
Mild enough to reconcile cleanly on stage, real enough that a chat upload can't do
it.

Regenerate it any time with:

```bash
python vp-workshop/scripts/make_messy_data.py
```

(Source data: `part3-abbey-road/data/streams.csv`, Jan-Mar 2025.)

## Before the session (do not skip)

1. **Subscriptions.** The desktop app needs a paid plan (Pro/Max/Team/Enterprise)
   per attendee. Confirm every participant is provisioned and signed in
   beforehand. This is the #1 thing that eats the first 15 minutes.
2. **Pre-work email (3-4 days out):** install the Claude Code desktop app, sign in
   with the Anthropic account, confirm the **Code** tab loads. No git, and nothing
   to download up front -- they open an empty folder; the only download is today's
   data in Segment 3 (or the zip, if you use that fallback).
3. **Permissions mode:** set **Auto-accept edits** for the live flow so files
   write without a prompt every time. Mention that "ask first" is the normal
   default they'd keep day to day.
4. **Windows:** local sessions need Git installed (Macs are fine out of the box).
5. **Room:** a projector for show-and-tell, and 2-3 people lined up who are willing
   to share their screen.

## Facilitator beats

- **After Segment 1**, do a show-and-tell: ask two volunteers to share screens.
  Everyone's calculator looks different because the prompts differed. That *is*
  the lesson about prompting.
- **During Segment 3**, narrate the moment Claude runs code and corrects itself.
  That self-checking loop is the headline; don't let it slide by silently.
- **Float constantly.** Help anyone stuck, especially on phrasing. The failure
  mode for non-coders is over-thinking the prompt -- nudge them to just say what
  they want plainly.
- **Keep pointing at the table.** Every time something lands, name which row of
  the chat-vs-Code table it just proved.

## Dry-run checklist

Run the whole thing solo on a clean machine in the **desktop app** before game
day. Confirm: the confetti and meeting-cost builds render in the preview with no
manual steps; the live "remember this" preference request changes the next build;
in **Segment 3 the data prompt downloads the four files** on the room's network
(the likely failure point -- if github.com is blocked, switch to the zip); plan
mode works; Claude actually runs code and reconciles the files; `/refresh-report`
re-runs; and the finale deck flips with arrow keys. Time every segment and trim
until the core fits inside 50 minutes, leaving 10 for questions and the inevitable
hiccup.
