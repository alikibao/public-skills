# Proof-of-Concept Studio — the presentation room

In a spreadsheet, the safest name wins. In context, names come alive. Most clients have
little practice making creative decisions, so the agency never hands over a bare list: it
puts every name into the world first — a premium print ad, a news headline, a product on
a shelf — and checks internally that each one passes a single test before any client
sees it: **in the first split second, do you lean toward believing it?**

**Inputs:** `00-intake.md`, `02-framework.md`, `07-final/finalists.json`, and the
screening files for domains and risks.
**Outputs:** `07-final/final.json` and `07-final/board.html`.

## Steps

1. **Write the context copy for each finalist:**
   - `descriptor` — ≤ 8 words that tell people what it is, so the name doesn't have to
     ("Feather — the lightweight fiber you need"). Consumers aren't stupid; a good
     descriptor lets the name stay surprising.
   - `headline` — a believable news headline about the launch.
   - `ad_line` — one line for a premium black-and-white print ad (e.g. "Mornings that run
     well run on Feather.").
   - `story` — 2–3 sentences: what the name says and why it's unexpected here.
   - `in_use` — the name in a real sentence someone would say or text.
   - `domain` — the best realistic domain from screening.

2. **Run the believability test.** Read each name in its contexts. Mark `believable`
   as `yes`, `stretch` or `no`. For a stretch, try a better descriptor first — often the
   descriptor carries the category so the name can stay bold. If a name is still a `no`,
   tell the lead rather than quietly dropping it.

3. **Write `final.json`** in the schema documented at the top of
   `<skill-dir>/scripts/build_board.py`. Carry over `type`, `territory`, `zone`, `gut`,
   `recommended`, `says` and `risks` from the finalists, and `off_table` too. Put the
   recommended names first.

4. **Build and check the board:**
   ```
   python <skill-dir>/scripts/build_board.py <ws>/07-final/final.json --out <ws>/07-final/board.html
   ```
   If you can, screenshot it and look: every name should read cleanly in every tile.

Return to the lead: which names are `stretch` or `no` and why, in a few lines.
