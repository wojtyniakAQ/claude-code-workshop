# 3 · The real difference (20 min)

This is the part you can't do by dropping a file into a chat window.

Work through it in five steps.

## 3a · Grab today's data

First, get the messy files -- **three signup exports from three different
systems** that are all supposed to be the same event's attendee list, plus a
human `notes.txt` explaining the quirks. Different column names, different
date formats, some junk rows -- and the same person shows up more than once,
spelled differently each time. Exactly the kind of mismatched mess that lands
on your desk in real life.

Open your browser (not Claude) and go to:

> https://wojtyniakaq.github.io/claude-code-workshop/data/

Click **Download all (zip)**, unzip it, and drop the `data` folder into your
workshop folder. This is a normal browser download, so there's nothing for
Claude to ask permission for -- you're just adding files to a folder it can
already see.

Ignore the **"Not yet"** box at the bottom of that page. There's a second file
down there for later; grabbing it now puts the wrong number on your screen for
the rest of this exercise.

(If the wifi is being difficult, ask your facilitator for the backup zip.)

## 3b · Let Claude read the whole pile

> Look through everything in the `data/` folder -- there are three signup
> lists from different systems and they don't quite match, plus a notes.txt.
> Tell me in plain English what's in there and where the files disagree.

Notice it read **all** the files at once, and the notes, and figured out the
mess. A chat upload takes one file at a time.

## 3c · Plan before the big build

Turn on **plan mode** (toggle it on in the app -- now Claude plans first and
won't build until you say go), then paste:

> I want to reconcile these three exports into one clean attendee list --
> figure out which rows are actually the same person under different
> spellings or typos, and drop anything that's obviously junk, not a real
> person. Then build me an interactive app: a single self-contained HTML
> file with a searchable, sortable table of the final list, counts by team,
> and a panel showing which records got merged into which person and why, so
> I can double-check the calls. Don't build yet -- lay out your approach so I
> can adjust.

Read the plan. Change one thing (e.g. "also show me the raw row count before
and after"). Then approve.

> Rule of thumb: use plan mode for anything bigger than a quick tweak. It's
> cheap to throw away a plan and expensive to throw away work -- and you get
> to steer before anything is built.

## 3d · Let it build (and watch it run real code)

Claude will now **write and run actual code** to compare every row across
the three files, match people whose names were typed differently, and throw
out the junk. If it hits a snag, watch it fix itself and re-run. That
self-correcting loop -- doing the work and checking its own answer -- is the
thing a chat can't do.

When the app appears in the preview: search for a name, sort the table,
click into the merge-audit panel and find a person who was merged from two
or three rows. Then reshape it by talking:

> Add a count at the top showing how many raw rows came in and how many real
> people came out.

> Let me filter the table by team.

This is the payoff: you started with 58 messy rows spread across three
systems, and you end with a defensible list of 41 real people -- and for
every merge, you can see exactly why Claude called it the same person.
That's not a guess you have to trust. It's an answer you can audit.

**Chat hands you a picture. Claude Code hands you a working app.**

## 3e · Turn it into a command you keep

> Save this whole reconciliation as a custom slash command called
> `rebuild-list`, so I can run it again later on whatever files are sitting in
> the `data` folder at the time.

(If Claude describes what it's about to create and asks whether to go ahead,
just say "yes, create it" -- it's all one conversation.)

**There is no button to look for.** What you made is a *command*: type `/` in
the message box and `rebuild-list` is now in the list, alongside the ones that
shipped with the app. That's how you run it. It's saved in your project, so
it's still there tomorrow.

## 3f · Now prove the command actually does something

More people signed up after those exports were pulled. Go back to the download
page -- the **"Not yet"** box at the bottom is for now:

> https://wojtyniakaq.github.io/claude-code-workshop/data/

Download **`late-signups.csv`** and drag it into your `data` folder, alongside
the other files. That's it, just move the file.

Then run it -- type:

> /rebuild-list

Watch the headcount go from **41 to 47**, and look at the merge panel again:
three of the nine late signups weren't new people at all. One had signed up
under a nickname, one through the system with the typo'd domain, and one with
their email in capitals. Claude caught all three and merged them instead of
double-counting.

That's the whole point of a saved command. Next week you re-pull from the
three systems, drop the fresh exports into `data`, run it again, and you get a
current list without redoing any of the thinking.

## If something looks off

This is real reconciliation, so it's normal to spot something you'd push
back on. For example:

> You merged "Pip Ashworth" and "Philippa Ashworth" into one person -- how do
> you know that's not two different people who happen to share a last name?

Ask Claude to show its reasoning for that specific merge (it should point to
the matching email). If the email doesn't match, tell it to split them back
out. The point isn't that Claude is always right -- it's that you can ask
"why" and get a real answer, then correct it in plain English.
