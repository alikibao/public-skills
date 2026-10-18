---
name: hit-products
description: Shape, test and grow products people love and keep coming back to, using the hit-making playbook Mark Pincus (Zynga, FarmVille) lays out in "Life at the Speed of Play". Separate the winning instinct from the likely-wrong idea, break each idea into Proven / Better / New, test the risky part with the cheapest probe instead of an MVP, grade honestly whether it's an A or a B+, and design for engagement and retention (core loops, social mechanics, Bold Beats, day-365 thinking). Use whenever someone has a product, app, startup or feature idea, asks "will this work" or "what should I build", wants to validate, pivot or kill an idea, is planning an MVP or launch, wants to understand why a competitor or hit product works, or is chasing product-market fit, or wants a product to be more engaging, sticky, fun, social, viral, gamified or retentive, even if they never mention Pincus or frameworks. Works for consumer, prosumer, AI and B2B products. Not for naming (use business-naming), visual design or writing the code.
---

# Hit Products

A product-making method distilled from Mark Pincus's book *Life at the Speed of Play*
and his conversation about it on Lenny's Podcast. Pincus founded Zynga and several
other companies and claims a hit rate on major game launches far above the industry's.
His argument is that the hit rate came from a repeatable process, not from genius.

The whole method rests on one asymmetry: **a good product maker's instinct is right
almost all the time (his estimate is ~95%), but any specific idea built on it is
usually wrong (right ~25% of the time at best).** Everything below follows from that:

1. **Hold the instinct tightly and the idea loosely.** Generate several ideas on top
   of one instinct and expect most to die.
2. **Copy what is proven, improve what you can, isolate what is new.** Most products
   fail for the wrong reasons, because they reinvented things that already worked.
   The genuinely new part is the riskiest part, so it gets tested on its own.
3. **Test the idea, not a product.** Find the smallest thing that can give real
   signal: a link, an ad, a mock, a hand-run service. A "viable" product is usually too
   big and too late.
4. **B+ is the enemy of A.** A good-enough idea attracts money, users and staff and
   keeps hope alive for years. Recognize B+ early and keep moving.
5. **Retention beats virality.** Ask whether people will still be using this in a
   year, and design for that from the start.
6. **Being right beats scale.** Stay close to the product and the user, and keep
   asking what the users will thank you for.

`references/principles.md` holds the reasoning behind these. Read it once at the start
of any substantial session. The other reference files are loaded as each phase needs
them.

## Your stance

Act as an experienced, candid product partner. The user may be emotionally invested,
and the most useful thing you can do is be intellectually honest: name the instinct,
call a B+ a B+, say which part is untested hope. Do this warmly and without cynicism.
The point is to help them reach an A faster.

Know where you are strong and weak, because the book tested this directly with an LLM:

- **Strong:** deconstructing what already works (the *Proven*). Use research (web
  search if available) to do this properly.
- **Weak:** telling *Better* from *New*. Models (like most people) label new ideas as
  "better". Run the 10-out-of-10 test on every Better item, and move anything that fails
  it to New.
- **Weak:** truly novel *New*. Your first New ideas will be conventional. Push past them
  (see the moves in Phase 2) and offer several, labelled as bets.
- **Cannot do:** create signal. Only real users can. Every plan you make ends in a
  cheap real-world test with a threshold set in advance, never in "launch and see".
- **Easily stale:** your knowledge of who's in the market. Categories move fast, and a
  variant you propose may already exist or have died. Check what exists *now* (web search
  when available), cite sources, date your claims, and mark anything unverified. One
  well-sourced competitor fact is worth more than five plausible ones.

## Pick the entry point

| Situation | Path |
|---|---|
| New product, startup or feature idea; "what should I build"; "help me shape this" | **Full path**, Phases 0–6 |
| "Is this idea good / will it work / should I keep going?" | **Idea review**: a light Phase 0, then Phases 1, 3 and 4 on their idea, plus a test plan (Phase 5) |
| "Why did X work?" / competitor or hit teardown | **Teardown**: `references/proven-better-new.md` → teardown template |
| Existing product: engagement, retention, growth, monetization, "make it more fun/sticky" | **Engagement audit**: `references/engagement.md` |
| Building on a new platform (AI agents, voice, XR, crypto, robotics) where little is proven | Add `references/new-platforms.md` to whichever path applies |
| Running a product team: roadmap, prioritization, OKRs, too many small features | `references/roadmap.md` |

In one line at the start, say which path you're taking. If the user wants something
quick ("just tell me if it's any good"), compress: give the instinct, the PBN table,
the grade and the first test, and skip the rest.

## The full path

### Phase 0: Intake

Ask everything in one round (AskUserQuestion if available, otherwise a short numbered
list). Where the user already gave an answer, confirm it rather than asking again.

- What they want to build, and **why**: the itch, the frustration, the thing they
  can't believe doesn't exist. Would they use it themselves every week? Products built
  for the maker's own need (a surf shop owner's storefront, a designer's design tool)
  start with a focus group of one who has taste.
- What they're an **expert witness** on: the problem, community or data they're closer
  to than almost anyone. That's usually where their instinct comes from and their edge.
- **Who exactly** it's for. Name a specific person or segment ("nurses in Indiana who
  play on their lunch break"), not "everyone".
- **Where** it will live: platform, channel, form factor.
- Stage and evidence so far: anything built, tested, measured? What did users actually
  *do* (not say)?
- Resources: time, team, money, and how long they can afford to be wrong.
- What winning looks like for them. A lifestyle business and an Internet Treasure (a
  service people can't remember life without) call for different choices.

Don't stall. If answers are thin, write down your assumptions and continue. The user
can correct them as they react to the work.

### Phase 1: Find the instinct, check the water

Separate the **instinct** from the **idea** in writing:

- *Instinct*: a human truth or missing thing, stated with no solution in it ("getting a
  ride should be as easy as sending a text"; "adults want permission to play").
- *Idea*: one specific way of building on it ("text a dispatcher to book a cab").

A good instinct statement could support five very different products. If yours only
supports one, it's still an idea, so dig a level deeper and ask what need it serves.
Note whether this is an **instinct vein**: a theme the founder keeps coming back to,
which could produce many products over a career.

Then check the **body of water** (the market). A great boat sits still on a dry lake
bed, and in the right water most boats float. Use the four tests in
`references/principles.md`: room to enter, a proven way to make money, room to
innovate, and long-term tailwinds. Also note what kind of water it is (platform shift,
mature market or new planet), because that changes how much *New* you need (see
`references/proven-better-new.md`).

### Phase 2: Shots on goal: several ideas on one instinct

Generate **3–5 idea variants** on the instinct, deliberately different from each other.
Their idea is one of them, and gets no special treatment. Include:

- **The embarrassingly small one**: one narrow use case, one audience, buildable in
  days. Many big products started as something that looked too small (a poker game on
  Facebook; a site for one college).
- **The near-copy**: take the hit closest to the instinct, keep almost all of it, and
  change one thing.
- **The latent-demand one**: a feature people already tolerate a clunky product to get
  (or a behavior they hack together by hand), rebuilt as the whole product.
- **The different-audience or different-platform one**: same instinct, aimed at
  someone or somewhere unexpected.

Moves for getting past conventional New ideas:

- Add a new dimension to a stale activity: make a solo activity social, make a static
  object interactive, make a virtual reward real.
- Find who is already living a primitive version of the future and hacking around the
  gap.
- Ask what changes if a scarce input became nearly free (tokens, listings,
  distribution).
- Pair a proven mechanic with whatever is trending in the audience's culture right now.
  Fast hypercasual game studios built hits this way.
- Play the **imagination chessboard**: write a short day-in-the-life of a user two years
  out, assuming everything went right. Then pull concrete use cases and features out of
  the story. Asking "what if everything goes right?" breaks limiting assumptions.
- Look for a feature that's buried or misused inside someone else's product and could
  be the whole product.

### Phase 3: Proven Better New

Read `references/proven-better-new.md`. For each variant, fill in:

- **= Proven**: the specific product(s) this audience already loves on this platform,
  and the exact mechanics, flows and details you will reuse. When you can, research the
  real products. If subagents are available, run one teardown per proven product in
  parallel, each following the teardown template. Be precise: proven means *this*
  audience on *this* platform. A 1990s hit on another platform doesn't count.
- **> Better**: improvements that 10 out of 10 current users of the proven product
  would agree are better (free, no download, faster, fewer clicks, works where they
  already are). Anything that fails that test goes to New. Look hardest at the **ask**:
  everything the product demands before it delivers (money, download, sign-up, setup,
  minutes per session, getting friends to join). Cutting the ask is the most reliable
  Better there is. Zynga's formula was a game people already knew, free, about three
  clicks to start, and 5–15 minutes a session.
- **+ New**: the novel, back-of-the-box reason anyone would try it. Assume it fails.
  Keep it isolated so it can be tested on its own, and line up a few alternative News.

Also research the **failed predecessors**: earlier attempts at this instinct, and what
killed them. That tells you which risks are real and which New to isolate. (Their makers
are often great hires, too.)

Flag the two classic errors as you go: **too much New** (reinventing everything, which
makes the product wide, shallow and confusing) and **fake Proven** (calling something
proven when it belongs to another platform, audience or era).

### Phase 4: Grade and choose

For each variant, give an honest letter grade and a one-line reason. Use the signal
checklist in `references/principles.md`. Remember that at this stage nothing has *true*
signal yet, so the grade measures how strong the bet is: the instinct, the water, how
much is Proven versus New, how cheap it is to test, whether people will still use it in
a year, and whether distribution is designed in.

Choose 1–2 variants to test first and keep the rest queued as the next shots. Say
plainly if the user's original idea isn't the strongest. A losing idea can hold a
winning instinct, and there's no honor in going down with it. Grade your own
recommendation too: give your confidence and the specific evidence that would raise or
lower its grade. Your favorite is also an idea, and probably wrong.

### Phase 5: Test plan: Minimum Idea State, not MVP

Read `references/testing.md`. For the chosen variants:

- Test the **New** first, because that's where the risk is. Proven doesn't need
  testing; Better needs light checking.
- Split the risks and give each its own test: demand (do people want it?), supply or
  content (will enough people contribute, will sellers show up?), and distribution (can
  you reach them cheaply?). A single test that mixes them can't tell you which one
  failed.
- For each test: the cheapest probe that could give real signal, who sees it, the
  **threshold set in advance** that means "heat", the **kill rule**, and a time box
  measured in days.
- Order the tests from cheapest to most expensive. Aim to run many in parallel, so the
  user is testing more ideas in a week than their industry tests in a year.
- Say what happens on success: build the real thing properly, and when conviction is
  earned, launch big (a Maximum Launch Product, not a timid MVP).

### Phase 6: Engagement and distribution by design

Read `references/engagement.md`. For the leading variant:

- The **core loop** (the action users will repeat), and what makes it satisfying.
- A **leading metric invented for this product**, one the team can move that predicts
  long-term retention (the way "round trips with a friend" did at Zynga). Also the
  D1 / D30 / D365 picture: why someone would still be here in a year.
- Social and emotional hooks that fit (reciprocity, expression, status, collection,
  progress), chosen because they serve the core loop, not stuck on top of it.
- The first **Bold Beats**: fast, isolated, killable experiments that could change the
  metrics.
- **Distribution built into the product**: where the audience already spends time, and
  how use itself brings new people. A plan that says "word of mouth" with no mechanism
  is hope.
- **Cold start**, if the product needs other people or content to be useful: the
  smallest dense unit to win first (one campus, one team, one neighborhood), and what
  makes it worth opening on day one before the network exists.

### Deliver the Hit Plan

Write the plan using `assets/hit-plan-template.md`. Use a document or artifact if the
environment supports one, otherwise a markdown file in the working directory. The
plan should be readable in about ten minutes. Put detail in tables, skip template
sections that don't drive a decision for this user, and put research sources at the end. In chat,
keep it short: the instinct, the recommended variant and its grade, the first test to
run this week, and the main risk.

## Other paths, briefly

**Idea review.** Run Phases 1, 3 and 4 on their idea as it stands, then give a test
plan. Lead with the grade and the reason. If it's B+, say what would have to be true for
it to become an A, and which alternative variant you'd test alongside it. Ask directly:
*Is this belief or hope?* Belief rests on things they've seen users do. Hope is
confidence with nothing under it.

**Teardown.** Deconstruct the product with the template in
`references/proven-better-new.md`: what it took from proven products (with sources),
what it made better, what was new, why it hit at that moment (platform shift?
distribution hack? latent demand?), and what that implies for the user's own product.

**Engagement audit.** Start with diagnosis before features: work out where users drop
off and whether each drop is a product problem or something engagement can't fix
(paywall, pricing, seasonality, acquisition mix). Check that the category's proven
basics are in place before inventing anything: onboarding, trial and paywall hygiene,
notification patterns. Products often fail for the wrong reasons. Then find the core loop and the
current leading metric, check retention at each horizon, and look for anti-patterns
(mouse-nuts features, monetization that squeezes the lemon, chores disguised as
engagement). Turn a request for one "big push" into several isolated, cheap experiments
with thresholds and kill rules, plus a better metric. Write it up with
`assets/engagement-audit-template.md`. Open and close with: *What will your users thank
you for?*

## Coaching language

Use these moves with the user. They keep the work honest without making it personal:

- "That's the instinct, and I think it's right. This is one idea on top of it. Let's
  see a few others."
- "Which part of this is genuinely new? Let's assume that part fails. How would we find
  out cheaply?"
- "Would 10 out of 10 people already using [proven product] call that better, or is
  it new?"
- "What would this look like if it were embarrassingly small?"
- "Is that belief or hope?"
- "If you're asking whether it's an A, it probably isn't yet. What would make it one?"
- "Will people still be using this in a year? Why?"
- "What will your users thank you for?"

## Reference files

- `references/principles.md`: instincts vs ideas, body of water, true vs false signal,
  B+, hope, ambition, taste. Read first.
- `references/proven-better-new.md`: the framework, contexts, worked examples,
  pitfalls, teardown template.
- `references/testing.md`: Minimum Idea State probes, thresholds, kill rules, failure
  machines, launching big.
- `references/engagement.md`: core loops, leading metrics, retention, the mechanics
  playbook, Bold Beats, social design, distribution, anti-patterns.
- `references/new-platforms.md`: building where nothing is proven yet (AI and beyond).
- `references/roadmap.md`: running a product team as a weekly learning machine.
- `assets/hit-plan-template.md`: the deliverable for new products and idea reviews.
- `assets/engagement-audit-template.md`: the deliverable for existing products.
