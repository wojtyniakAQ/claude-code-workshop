# 3 · The real difference (20 min)

This is the part you can't do by dropping a file into a chat window.

In your folder is a `data/` folder with **three monthly files that don't agree**
(`jan.csv`, `feb.csv`, `mar.csv`) plus a human `notes.txt`. Different column
names, different date formats, a missing week, some junk rows. Exactly the kind of
mismatched mess that lands on your desk in real life.

Work through it in four steps.

## 3a · Let Claude read the whole pile

> Look through everything in the `data/` folder -- there are a few files and they don't quite match, and there's a notes.txt. Tell me in plain English what's in there and where the files disagree.

Notice it read **all** the files at once, and the notes, and figured out the mess.
A chat upload takes one file at a time.

## 3b · Plan before the big build

Turn on **plan mode** (toggle it on in the app -- now Claude plans first and
won't build until you say go), then paste:

> I want to combine these files into one clean dataset and build me an interactive app -- a single self-contained HTML file with tabs, filters and a search box that update the charts live, sortable tables, click-a-bar-to-drill-down, and headline numbers that recompute as I filter. Don't build yet -- lay out your approach so I can adjust.

Read the plan. Change one thing (e.g. "add a 'top artists' tab"). Then approve.

> Rule of thumb: use plan mode for anything bigger than a quick tweak. It's cheap
> to throw away a plan and expensive to throw away work -- and you get to steer
> before anything is built.

## 3c · Let it build (and watch it run real code)

Claude will now **write and run actual code** to clean and combine the files. If
it hits a snag, watch it fix itself and re-run. That self-correcting loop -- doing
the work and checking its own answer -- is the thing a chat can't do.

When the app appears in the preview: click the tabs, type in the search box, sort
a table, click a bar to drill in. Then reshape it by talking:

> Add a toggle to compare the three months side by side.

> Let me search by artist.

**Chat hands you a picture. Claude Code hands you a working app.**

## 3d · Turn it into a button you keep

> Now make this a button I can press to rebuild the whole app next month when I drop new files into the folder. Call it `/refresh-report`.

(If Claude describes the button and asks whether to go ahead, just say "yes,
create it" -- it's all one conversation.)

Then run it:

> /refresh-report

Watch it redo the whole thing end to end. You didn't get a one-off report -- you
built a tool that lives in your project and runs again whenever you want.
