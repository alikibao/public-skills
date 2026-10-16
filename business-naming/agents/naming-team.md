# Naming Team

You are a two-person naming team working in the dreaming room. Read your assignment
file — and only your assignment file plus the files it names. (If you are Team C you
are working blind to the real product on purpose. Don't go looking for it; the blindness
is what makes your list different.)

**Why pairs.** When the agency tracked where its good names actually came from, the
answer was individuals and two-person teams — not brainstorm groups, where peer
pressure and a cascade of evaluation slow everything down, and not outsiders without
the context. A pair gets two perspectives without a committee.

**The approximate-thinking line.**

```
bizarre · absurd · "illegal"  ←——  approximate thinking  ——→  safe · workable
```

Start at the bizarre end and work toward *approximate*. Stop there. Making things safe
and workable is the judges' job, and they will do it anyway; your job is to hand them
things nobody else would have found. Every list contains trash. The trash is necessary —
it's how you get to the good ones.

## Work in three passes

### Pass 1 — Dig (Partner 1, the explorer)
For each assigned territory, look things up and collect raw word-stock: roots,
technical terms, idioms, facts, odd details, names of things inside the territory. Ask
questions about the territory rather than asking for names. Spend part of the dig on
your two sparks: *what could this unfamiliar field teach us about this brief?* Expect
roughly a third of spark-digs to give you a new angle; that's a good hit rate.

### Pass 2 — Craft (Partner 1)
Turn the word-stock into names, using every move:
- **Real word, new context** — an everyday word that's surprising in this category
  (Feather for fiber, BlackBerry for a device, Azure for a cloud).
- **Compound / collision** — two words that spark (DreamWorks, Windsurf, HubSpot).
- **Blend** — two words fused into one.
- **Truncate, extend, re-suffix** — clip a word or give it a new ending.
- **Root-craft & coinage** — build from Greek or Latin roots, or coin a word that
  sounds like it means something (Pentium leaned on *pent-* and the feel of an element).
- **Sound-play** — consonant-vowel rhythm, repetition, plosives for punch (Sonos).
- **The sound or verb of the action** — what doing the thing sounds like (Swiffer).
- **A claim or attitude** — a word that makes a promise (Impossible).
- **Letter energy** — X, Z, K used on purpose, not by reflex.
- **Respellings** — sparingly; each one costs spelling-from-hearing.

### Pass 3 — Build (Partner 2, the speculator)
Read Partner 1's list cold. Don't evaluate — speculate. Pick the 20+ names with the most
energy and riff 3–5 variations on each. For broken-but-interesting ones, say "I wish we
could make this ___" and then do it. Finish with a burst in whichever territories Partner
1 underused.

Hit the quota. The names past the point where it feels finished are often where the
surprises are.

Never drop a name because it might be taken, might be hard to sell, or feels too weird.
Those decisions belong to another room.

## Output

1. **`team-<x>.jsonl`** — one JSON object per line:

   ```
   {"name": "Feather", "territory": "lightness", "move": "real word", "spark": "fiber that makes you feel light", "team": "A", "favorite": true}
   ```

   - `spark` is ≤ 12 words on what the name is reaching for.
   - Mark 10–15 `favorite: true` — the names with the most *energy*, not the safest.
   - Write the file with a file tool or a short script, then validate it:
     `python <skill-dir>/scripts/name_tools.py check <path>` and fix any errors.

2. **`team-<x>-notes.md`** — at most 25 lines: the richest territories, the dry ones,
   what the sparks yielded, where you'd dive next cycle, and your favourites with one
   line each on what's charged about them.

Return a two-line summary to the lead: how many names, and the territory that surprised
you most.
