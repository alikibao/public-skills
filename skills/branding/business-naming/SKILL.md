---
name: business-naming
description: Name a business, startup, product, app, service, feature or brand the way a top naming agency does - category and customer research, a creative framework, three independent naming teams run as subagents, a separate judging room, linguistic and trademark screening, and a proof-of-concept board that shows each finalist in real-world context. Use whenever someone wants name ideas, is stuck choosing a name, wants candidate names rated or compared, is weighing whether to rename a company or product, or needs a descriptor or tagline to sit beside a name - even if they only say "what should I call this". Not for naming variables, files or other code identifiers.
---

# Business Naming

A naming process modelled on how a leading naming agency describes its own work
(the firm behind names like Swiffer, BlackBerry, Pentium, Sonos, Azure, Impossible
and Windsurf). The principles are distilled in `references/method.md` — read it once
at the start of every project, because every role below leans on it.

The core belief: anyone can now generate 300 names in a minute, so a long list is
worth almost nothing. The value is in three things a list can't give you:

1. **A strategy sharp enough to aim at** — what the name has to say, and where we are
   *not* going.
2. **Genuinely divergent generation** — independent teams with different perspectives,
   producing far more names than feels necessary, without judging while they dream.
3. **Disciplined judging** — separating the *right* name from merely good ones, in a
   different room from the one where names were made.

## What a right name does

A right name does three jobs: it **gets attention**, it **holds attention** (it is
processing-fluent — easy to say, with something inside the brain can grab), and it
**surprises** (original in its category and unexpected *from this company*). The
target is *surprisingly familiar*. Comfortable names feel safe, test well, and then
vanish — that is the comfort trap, and most of this process exists to escape it.

## Pick the entry point

| Situation | Start at |
|---|---|
| New company, product, app or feature needs a name (default) | Phase 0, run everything |
| User has an existing name and wonders whether to change it | `references/renaming.md`, then the full project only if the case holds |
| User already has candidates and wants them judged | A light Phase 0 (what it is, markets, the four questions), then Phase 4 with their names → screening → board. Offer a small Team A cycle if they want alternatives |
| Name is chosen; they need a descriptor, tagline or naming system | Phase 6 only |

**Depth.** Run *Standard* (two generation cycles) by default. Run *Sprint* (one cycle,
smaller quotas) when the user wants speed or says "quick". Say which depth you're
running in one line at the start.

| | Sprint | Standard |
|---|---|---|
| Generation cycles | 1 | 2 |
| Names per team per cycle | 80+ | 150+ (cycle 1), 100+ (cycle 2) |
| Shortlist sent to screening | ~15 | 25–30 |
| Finalists presented | 8–10 | 10–15 |

## The agency: rooms and roles

You are the **project lead**. You talk to the user (the client), write the briefs,
run the rooms in order, and keep generating and judging apart. Each specialist has a
brief in `agents/`.

| Room | Role | Brief | Runs |
|---|---|---|---|
| Discovery | Landscape Scout | `agents/landscape-scout.md` | parallel with Insight Analyst |
| Discovery | Insight Analyst | `agents/insight-analyst.md` | parallel with Landscape Scout |
| Strategy | You + the user | this file, Phase 2 | — |
| Strategy | Cartographer | `agents/cartographer.md` | after the framework |
| Dreaming room | Naming Teams A, B, C | `agents/naming-team.md` + one assignment each | parallel, isolated |
| Judging room | Judge | `agents/judge.md` | twice: shortlist, then finals |
| Screening | Linguist | `agents/linguist.md` | parallel with Screener |
| Screening | Trademark & Availability Screener | `agents/trademark-screener.md` | parallel with Linguist |
| Presentation room | Proof-of-Concept Studio | `agents/poc-studio.md` | last |

Below, `<skill-dir>` is the folder this SKILL.md lives in and `<ws>` is the project
folder. Pass both, as absolute paths, to every role.

**Running the roles.** When an Agent/Task tool is available, run each role as its own
subagent, and launch roles marked *parallel* in the same turn. Subagents can't see this
conversation, so everything they need must be in files in the project folder. A prompt
like this works:

> Read `<skill-dir>/agents/judge.md` and follow it. Mode: shortlist. Skill directory:
> `<skill-dir>`. Project folder: `<ws>`. Inputs: `<ws>/02-framework.md`,
> `<ws>/05-judging/merged.json`. Write your output to `<ws>/05-judging/`.

If you can continue an agent later (e.g. a SendMessage tool), reuse
the Judge for the finals so it keeps its reasoning.

**No subagents?** Play each role yourself in sequence, reading its brief first. For
Team C, write the analog assignment and generate from it *before* re-reading the
product files, so its perspective stays genuinely different. Keep the dreaming and
judging passes as separate steps — never cut names while generating.

**Project folder.** Create `naming-<slug>/` in the working directory:

```
naming-<slug>/
  00-intake.md
  01-research/        landscape.md, insight.md
  02-framework.md
  03-map.md, 03-sparks.txt
  04-dream/c1/        assignment-a.md, team-a.jsonl, team-a-notes.md, ... (c2/ for cycle 2)
  05-judging/         merged.json, longlist.md, shortlist.json
  06-screening/       linguist.md/.json, trademark.md/.json
  07-final/           finalists.json, final.json, board.html, report.md
```

Set up a task list with one item per phase so the user can see progress.

## Phase 0 — Intake

Gather everything in one round (AskUserQuestion if available, otherwise a short
numbered message). If the user already said most of it, confirm your reading and fill
gaps instead of re-asking.

- What it is, what it does, who it's for, what stage it's at.
- Markets and languages the name must work in (drives linguistic and trademark checks).
- The **four questions**: *How do you define winning? What do you already have that
  helps you win? What do you need in order to win? What does the name need to say —
  or help you say?*
- Constraints: domain needs, length, words to avoid, the parent brand and its existing
  names ("unexpected" is relative to the company — Azure surprised coming from
  Microsoft; from a company known for playful names it wouldn't have).
- The current name and its history, if this is a rename.

Don't stall on the four questions. If the user can't answer them, draft answers from
what you know (and from research, once it's in) and let them react. Founders often
discover they define "winning" differently from each other — surfacing that is worth
the question by itself. Write `00-intake.md`.

## Phase 1 — Discovery (parallel)

Spawn the **Landscape Scout** and **Insight Analyst** together.

- `landscape.md`: names in the category classified by type, the patterns that make up
  the category's "sea of sameness", a *not-going-there* bucket, white space, and what
  would be unexpected from this particular company.
- `insight.md`: a raw list of everything the product has, what customers need and say
  in their own words, the emotional truths of the category (nobody *wants* to mop),
  and benefit ladders climbing to 3–5 candidate **ultimate benefits** (fiber → regular
  → healthy gut → *I feel lighter*).

## Phase 2 — Strategy: the creative framework

Write `02-framework.md` yourself from intake and research. Think of it as a window the
teams walk through, not a checklist they must conform to — so keep it short (one page):

- Positioning in one line, and the **ultimate benefit** chosen (plus a runner-up).
- What the name must do (2–4 jobs) and the *not-going-there* bucket.
- **Desired feel** in a few plain words (e.g. "fast, reliable" or "light, warm") — the
  Linguist scores sound symbolism against it.
- The **surprise test**: what would be unexpected in this category *from this company*.
- Name-type range (real word in a new context → compound → coined). Descriptive names
  only if something exceptional demands clarity; the descriptor can carry the category.
- Hard constraints.

Then spawn the **Cartographer**. First draw random far domains for synchronicity —
`python <skill-dir>/scripts/name_tools.py sparks --n 6 > <ws>/03-sparks.txt`. A script
gives real randomness; picks you make yourself drift
toward the familiar. If a name vault exists (see below), give it to the Cartographer as
one more territory. The map (`03-map.md`) covers the whole ocean before anyone dives:
30–50 territories with raw word-stock, analog categories for Team C, twist options for
Team B, and a suggested split.

**Checkpoint.** Show the user, compactly (≤ 20 lines): the ultimate benefit, the
not-going-there bucket, the desired feel, and the three team setups you plan. Ask
whether anything is off before the teams start — this is the cheapest moment to
redirect. If the user said to just run it, state your choices and carry on.

## Phase 3 — The dreaming room: three teams

Write one assignment file per team in `04-dream/c1/`. The agency found good names
come from individuals and pairs, not brainstorm groups (peer pressure, evaluation
cascades) — and that three teams looking from three different angles produce three
genuinely different lists. That difference is the whole point, so protect it:

- **Team A — Insiders.** Knows everything: intake, research, framework, its share of
  the map. Names straight at the strategy.
- **Team B — The Twist.** Same product, plus one deliberate perspective shift: an added
  ingredient or feature, an amplified benefit, a different user or moment of use (the
  agency's example: the fiber product *also gives energy*). Pick the twist that pulls
  toward a plausible future of the brand. Gets different territories from Team A.
- **Team C — Outsiders.** Never told the real product. Gets only an analog brief: a
  different category that shares the ultimate benefit or emotional truth (fiber →
  *feeling lighter* → athletic performance gear). Their names get transplanted later,
  which is where many surprises come from. Its assignment must not mention the real
  product, company or category.

Each assignment contains: the brief for that team, its territories with word-stock
pointers, two random sparks each (draw fresh with the `sparks` command), the quota,
output paths, and the skill directory. Spawn A, B and C in parallel. Each writes
`team-x.jsonl` and `team-x-notes.md`.

Why the quotas are high: quantity leads to quality. Amateur lists stop at 50–100 names,
which is exactly where everyone else stopped too. The agency works through roughly
2,000 per project; the trash is necessary.

## Between cycles — sonar and redial (Standard only)

Merge and read the sonar:

```
python <skill-dir>/scripts/name_tools.py merge "<ws>/04-dream/c1/*.jsonl" --out <ws>/05-judging/c1-merged.json
```

It reports names per team and territory, favourite rates (a rich vein), dry
territories, and **cross-team collisions** — names two independent teams both reached.
Treat collisions as a warning that the name is probably the obvious move, not as a
vote in its favour. Read the team notes, then decide per team: **keep** (assignment
working), **redial** (change the assignment — new twist, new analog), or **dive** (go
deeper on a vein that showed gold). Like mapping a seabed before diving, cycle 2 goes
where the sonar showed something, plus one long-shot territory nobody tried.

Optional user check-in: share 10–15 *directions* — territories with two or three
example names each — framed as speculation, not a shortlist. Ask only whether there's
a vein to dive deeper into or avoid. Don't ask them to pick favourites yet: early
voting pulls everyone into the comfortable zone.

Write cycle-2 assignments in `04-dream/c2/` (new sparks, notes from cycle 1 included)
and spawn the teams again.

## Phase 4 — The judging room: shortlist

Merge everything:

```
python <skill-dir>/scripts/name_tools.py merge "<ws>/04-dream/**/*.jsonl" --out <ws>/05-judging/merged.json
```

Spawn the **Judge** in *shortlist* mode. The Judge never generated these names, which
is the point. It culls to names with energy, maps them into zones (invisible / tension /
noise), scores them on `references/evaluation.md` with gut scores of 1–10 and **no
sevens** (a seven is a way to avoid deciding), and writes a shortlist with a spread of
name types, all teams that earned a place, and at least two names expected to
polarize the client. The longlist is kept so names can come back later.

## Phase 5 — Screening (parallel), then finals

Spawn the **Linguist** and the **Trademark & Availability Screener** together on
`shortlist.json`. Both follow one rule taken from the agency: when a name hits a
problem, don't just kill it — ask *"how could we modify it so it works?"* (a respelling,
a compound, a descriptor, a neighbouring root) and propose the fix.

Then run the **Judge** in *finals* mode with the screening results. It picks the
finalists, applies screening (modified, kept with a noted risk, or moved off the table),
and lists a few strong *off the table — for now* names. Read `finalists.json` yourself
before going on: the list should be one you'd defend in front of the client, include
real range, and contain names that make you a little nervous.

## Phase 6 — The presentation room: proof of concept

Never present a bare list. People rarely practise making creative decisions; in a
spreadsheet, the safest name wins. In context, names come alive.

Spawn the **Proof-of-Concept Studio**. For each finalist it writes a descriptor that
carries the category (Feather — *the lightweight fiber you need*; the agency's Swiffer
leaned on a "quicker picker-upper" style line), a believable news headline, a premium ad
line, a short story of why this name, and a line of it used in real life — then runs the
one internal test that matters: *in the first split second, do you lean toward
believing it?* It builds `final.json` and runs:

```
python <skill-dir>/scripts/build_board.py <ws>/07-final/final.json --out <ws>/07-final/board.html
```

Look at the board (screenshot it if you can) before showing anyone.

## Phase 7 — The client room

Deliver two things:

1. **The board** — publish it as an artifact if the environment supports artifacts
   (follow that tool's own instructions); otherwise send the HTML file.
2. **A naming report** — a document in whatever format the environment prefers for
   documents (a docs artifact or connector if one exists, otherwise markdown). Contents:
   the framework in brief; the process in numbers (names per team and cycle, territories
   explored, how many screened); finalists with rationale, zone, scores and risks;
   off-the-table names; next steps — attorney clearance in each market, native-speaker
   checks, domain and handle acquisition, a quick test of recall and spelling-from-hearing
   with real people.

In chat, keep it short: the two or three you'd recommend and why, and that the
tension-zone names are in the set on purpose.

**Handling reactions** — this is where great names die, so it gets care:

- Start with curiosity: "That's interesting — what's the reaction underneath?" Separate
  *I don't like it* from *it doesn't do the job*.
- A polarizing name has energy. A name nobody objects to is usually invisible. Use the
  user's own reactions to explain the comfort trap.
- Move rejected strong names *off the table for now*, not into the bin, and bring them
  back once the user has lived with the shortlist for a while. Every name the agency
  is famous for was rejected at first (BlackBerry was dismissed in the first meeting and
  won on the second pass — partly because big competitors would never have dared).
- Turn objections into problems: "I wish it felt less clinical" becomes the brief for a
  targeted mini-cycle (one team, ~60 names in that vein, then Judge and screening on the
  new candidates only).
- Don't oversell. The user decides. Your job is that they decide with the strongest
  options in front of them, seen in context.

Optional follow-ons once a name is chosen: nomenclature (descriptor, positioning line,
how sub-products get named), a rename launch story (`references/renaming.md`), and a
simple 90–120-day tracking plan (unaided recall, spelling-from-hearing, search share).

## The name vault

Strong names that don't fit this project are assets. The agency files names under
abstract qualities rather than categories — names made for a small car sit beside names
made for a small processor — so they cross-pollinate later. At the end of a project,
save 20–40 of the best unused names tagged by quality (*small, fast, light, reliable,
warm, bold…*), one line each. Keep the vault where it will persist: a project document
called `name-vault.md` if a Projects tool is available, otherwise ask the user where
they'd like it. At the start of the next project, hand the vault to the Cartographer.

## Honesty and limits

- Trademark, domain and handle checks here are **preliminary knockout screens, not legal
  clearance**. Say so in the report and on the board, and recommend an IP attorney in
  each market before money is spent.
- A model's slang and connotation checks can miss things; recommend native-speaker
  checks for every serious market.
- Sound symbolism describes tendencies, not laws. Use it to tune and break ties, never
  to veto a name with meaning and energy.

## How to talk about names (all phases)

Use the agency's coaching language with the user and in every brief, because it keeps
people generating instead of defending: "That's interesting." "I wouldn't have thought
of that." Turn a kill into a problem — "I wish we could make that easier to spell",
"How could we modify that word so it's legally available?" During generation, nobody
evaluates; they speculate. Judging happens later, in its own room.

## Reference files

- `references/method.md` — the principles behind every phase (read first)
- `references/evaluation.md` — the rubric, zones, red flags and gut-score rules
- `references/sound-symbolism.md` — processing fluency and what sounds tend to signal
- `references/territories.md` — where names come from: territory families, name types, moves
- `references/renaming.md` — whether to rename, and how to launch one
- `scripts/name_tools.py` — `check`, `merge`, `phonetics`, `sparks`, `handles`
- `scripts/build_board.py` — the proof-of-concept board
