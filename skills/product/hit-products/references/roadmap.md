# Roadmapping: The Product Team's Operating System

How Pincus ran Zynga's product teams so that the method above happened every week, not
just in a kickoff. Useful when the user leads a team, owns a roadmap, or complains about
slow learning, scattered priorities or too many small features.

## Contents
1. The roadmap as operating system
2. The roadmap line item
3. The weekly review
4. Goals and OKRs
5. Mouse nuts, boiling the ocean, and the Rule of Four
6. Altitude and the Penguin Effect
7. Spreading what works
8. Keeping leaders close to the product
9. Roadmap template

## 1. The roadmap as operating system

A roadmap is where strategy meets execution: which hills the team is taking, what
outcome each project should produce, and what it costs in engineering time. Pair it with
a standing weekly meeting that Pincus called the most important hour of his week, his
real board meeting. It works as both a report card and a diagnostic: are engineers
building things users actually want, and is the team learning fast enough?

His claim: with a good roadmap discipline, around **80% of engineering days are real
shots on goal** (features users might actually want), versus maybe 20% at a typical
competitor. That's a multiple on effective capacity.

Teams will try to cancel the meeting when they have nothing to show. That's exactly when
it matters most.

## 2. The roadmap line item

The atomic unit is usually a feature or experiment. Each line has:

- **Hypothesis**: what we believe and which objective it serves.
- **PBN tag**: Proven (copy), Better (polish) or New (experiment), so risk is visible.
- **Expected outcome (EO)**: a number on a named metric (e.g. +X daily installs, +Y%
  D7 retention, +Z turns per user).
- **Cost** in engineering days, so you get *expected outcome per engineering day*.
- **Owner**, ship date, kill rule.
- After launch: **actual vs expected**, and the lesson.

Tracking estimated against actual engineering days also makes the team better at
estimating over time.

## 3. The weekly review

Every team arrives with:

1. The hypothesis it tested, tied to its objective.
2. Expected outcomes per engineering day.
3. Actual metrics against expected.
4. What it learned and how that changes next week's bets.

Pincus's three aims for each review: is the product on track for its goals, is the team
creatively productive and efficient, and are new product leaders getting better? If a
team doesn't know its numbers or isn't signing up for growth, the meeting reconvenes
later in the week. Weeks of only tiny features are a warning sign: teams without big
ideas drown in small ones.

Operate on compressed time: a day is like a week, a week like a month. Elon Musk's
question applies: what did you get done last week?

## 4. Goals and OKRs

- One clear objective (the hill), a few measurable key results.
- Set ambitious targets (Zynga typically started from ~30% quarter-over-quarter growth)
  so teams can't simply repeat last quarter's tactics.
- Ground ambition in what's demonstrably possible: what the best competitor has achieved,
  or what's within the laws of physics, not wishful round numbers.
- **Don't change OKRs mid-quarter.** As the gap shows, teams must rethink and take
  *more* risk, the opposite of the usual drift toward safe, small features.
- Write Bold Beats into each team's quarterly goals.
- Reserve capacity for the future. Zynga's maxim: you're redlining if less than ~25% of
  engineering days go to future growth.
- Caveat from Pincus himself: OKRs suit decentralized teams running live products with
  their own P&L. They're often overhead for a single team going from zero to one, and
  can turn into corporate theater if done badly. Try them for one quarter.

**Stop time.** When the market shifts or new evidence lands, call a deliberate pause:
stop business as usual, re-check whether the path still makes sense, decide on any pivot,
then sprint at the clearer goal. Pincus did this early at Zynga, pulling the team off a
scatter of small apps to double down on the one game with traction. Some people will
resist. If the call is right, the team comes back more committed.

**Don't promise revenue from New.** Because most New fails, avoid committing projections
(to a board or the market) that depend on unlaunched products. Zynga's later slate of
heavily forecast new games is the cautionary tale.

## 5. Mouse nuts, boiling the ocean, and the Rule of Four

- **Mouse nuts**: tiny incremental features. They're measurable, safe and pointless.
- **Boiling the ocean**: projects so big they never ship and everyone forgets why they
  started.
- **Rule of Four**: everything costs twice as much and takes twice as long as planned.
  Spend that on mouse nuts and you've lost the quarter.
- The answer between the two is the Bold Beat (see `engagement.md`).

## 6. Altitude and the Penguin Effect

- **Say what altitude you're at.** 5,000 feet: features, UX, execution. 25,000 feet:
  how the pieces fit. 50,000 feet: vision and mission. Leaders who jump between
  altitudes without saying so look like they change their mind every week.
- **The Penguin Effect** (a term from Zynga's CTO Cadir Lee): teams that are either
  crushing it or in crisis won't step off the cliff to try something new. The moment one
  team tries something and it works, everyone copies it within the hour. So make the
  first jump cheap, visible and celebrated.
- The longer a team goes without shipping, the more pressure it feels and the more
  incremental it gets. Shipping small bold things often keeps that pressure from
  building.

## 7. Spreading what works

- **One shared roadmap and analytics system** across teams. Zynga's teams initially kept
  a private roadmap and a version "for Mark". Things changed when one team's viral
  breakthrough was visible to all and copied immediately.
- **Teaching hospital**: run product reviews with other team members and new hires
  watching around the room, so judgment spreads by observation.
- When a team wins, it **teaches** how it found the opportunity, estimated cost, chose
  metrics and iterated. Every winning feature becomes a case study and, if it holds, a
  Golden Mechanic.
- Teams that hit their numbers earn more resources. Reward outcomes, don't dictate the
  method.

## 8. Keeping leaders close to the product

Pincus's management principles, framed around one goal: get people to do the right thing
when you're not in the room.

- **Be in the room as long as you can.** Micromanaging is fine while you're the best
  player at the position. He ran daily stand-ups personally until about 50 people.
- **Founders approve what users touch.** Discord's founders reclaimed final say over
  every user-facing feature after realizing the most important UX calls had drifted to
  the most junior people.
- **Guard product time.** Aim for at least half (ideally most) of a leader's calendar on
  product: roadmaps, reviews, brainstorms, hiring product people. Squeeze press,
  conferences and investor meetings. "Don't be a fake CEO."
- **Make everyone the CEO of something** with real ownership, and give promising people
  bigger jobs early (battlefield promotions). Clone your judgment through a **tech
  assistant** who shadows you for a year.
- **Challenge assumptions, not judgment.** Questioning someone's assumptions is
  collaboration; questioning their judgment is personal.
- **Hiring for new products**: look for people who built a failed version of what you're
  building ("broken résumés"); the product they made is the best résumé. Hire outside
  leaders one level below the intended role so they earn credibility inside your product
  first.
- **Values are earned in the trenches**, and the best ones say how you win (Zynga's
  "innovate on social game mechanics").

## 9. Roadmap template

```
## <Product> roadmap — week of <date>

Objective (this quarter): <the hill>
Key results: <KR1> <KR2> <KR3>       Status: green / yellow / red
Capacity: <N> eng days this week; <% on future growth> (redline < 25%)
Bold Beat this quarter: <name> — target ≥25% try, ≥10% lift on <metric>

| Item | PBN | Hypothesis | Expected outcome | Eng days | EO / eng day | Owner | Ship | Kill rule | Actual | Lesson |
|------|-----|-----------|------------------|----------|--------------|-------|------|-----------|--------|--------|

Learned last week: <...>
Bets changed because of it: <...>
What will our users thank us for this week? <...>
```
