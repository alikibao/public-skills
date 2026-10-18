# Testing: Minimum Idea State

How to turn instincts into conviction cheaply. A distillation of Pincus's argument
against the MVP and for testing far smaller units of an idea.

## Contents
1. The MVP trap
2. Minimum Idea State
3. The probe menu, cheapest first
4. Designing a test
5. Reading the result
6. Failure machines and AI
7. From signal to a Maximum Launch Product
8. Cautionary cases

## 1. The MVP trap

The weak word in "Minimum Viable Product" is *viable*. In practice teams use it as a
reason to keep building: it isn't viable yet, so it can't launch. Months go into
something that has close to zero chance of being right the first time. Viability is
also where hope comes from: if it's viable, it *might* work.

Two different things get blurred:

- A **learning product** exists to get signal on an idea. It can be fake, ugly, manual
  or broken after ten clicks.
- A **launch product** is something you already believe (from evidence) will be a hit.

Be explicit about which one you're building. Most of the time early on, it should be
the learning one, and it should be much smaller than people think.

## 2. Minimum Idea State

A **Minimum Idea State (MIS)** is the smallest expression of an idea that can be put in
front of the target audience and give directional signal. It isn't a product. It can
be a link, a slide, a video, a hand-run service or vibe-coded demoware.

Pincus's line on the podcast: build it wrong before you know it's right. Assume the current version is the wrong
product. If you believe that, you'd rather waste a day than three months on it.

## 3. The probe menu, cheapest first

| Probe | What it is | Good for | Book/podcast examples |
|---|---|---|---|
| **Listen first** | Ask target users what they did today, what frustrated them, what they use now, then stay quiet. Have no idea to defend yet. | Finding the real problem and latent demand before ego is invested | Emmett Shear (Twitch): gather data before having the idea, because nobody improves an idea they're already attached to |
| **Story test / focus group of one** | Tell one perfect representative of the audience a 30-second user story and watch their reaction | Fast read on adrenaline, i.e. whether they start inventing what happens next | Pincus pitching a game twist to two 13-year-olds on a gondola |
| **Fake door** | A link, button, menu item or dialog for a feature that doesn't exist; measure clicks | The appeal of a New idea inside an existing product or audience | A five-word link in Mafia Wars (Zynga's crime game), shown for one minute, clicked by ~23% of players, led to a poker crossover and a million installs in a week. A one-hour dialog-box test could have saved six months on Words With Friends' failed fast mode |
| **Ad / message test** | Run several ads or headlines to the target audience | Which promise, audience or variant has heat, before building | Pincus notes on the podcast how often teams never test their ads before launch |
| **Locked teaser** | Show the coming feature or content locked in the product, with "get early access" | Demand, positioning and even pre-revenue at once | A locked expansion on the FarmVille board tested art and messaging, and sold millions of dollars of early-access keys |
| **Landing page / waitlist / demo video** | Describe or show the product as if it exists | Whether the concept pulls sign-ups | Dropbox's demo video |
| **Ripomatic** | Mash up screenshots and screen recordings from existing products, with annotations and realistic copy, into a click-through story of the user experience | Conveying a new concept built largely from proven parts; getting feedback without code | Zynga's slide decks; a sitcom pitched as four key scenes instead of a full pilot script |
| **By hand (concierge)** | Deliver the experience manually before building software. Humanize before you productize | Learning what users value; getting the first superfans | Airbnb's founders photographing hosts' apartments and fixing the calendar in two days; DoorDash's Google Forms; Zappos buying shoes at retail; cable video-on-demand tested by someone roller-skating to a VHS deck |
| **Vibe-coded demoware** | A working prototype built with AI in hours, good enough for the demo path only | Interactive concepts, delight, onboarding flow | Interactive ripomatics |
| **Isolated hack in a live product** | A Bold Beat: a quick, hacky, isolated version of a big feature, shipped to real users | Big swings inside an existing product | See `engagement.md` |
| **Piggyback platform test** | Launch a tiny version where a captive audience already is (a platform, a community, another product's surface) | Distribution and real usage without building plumbing | Zynga building small apps on the newly opened Facebook platform instead of buying an audience |

Rule of thumb: if a probe will take more than a week, look for a cheaper one that tests
the same risk.

## 4. Designing a test

For every test, write down before running it:

1. **Hypothesis**: the single New element being tested, and the audience.
2. **Probe**: from the menu above. Use the cheapest one that real target users will see.
3. **Signal metric**: the user *behavior* that would count: click-through, sign-up,
   repeat use, invite sent, payment, return next day. Opinions ("would you use this?")
   are weak. Behavior is strong.
4. **Threshold**, set in advance, for "heat" and for "kill". Calibrate it against the
   proven baseline where possible. Reference points from the book: an in-game link
   clicked by about 23% of players justified building; a quarter of poker players
   joining friends' tables signalled the social idea worked; a Bold Beat needed ~25% of
   users to try it and a ≥10% move in a key metric.
5. **Time box**: days, not months.
6. **Next step on each outcome**: heat → build it properly; mixed → change one variable
   and rerun; no heat → kill it and run the next queued idea.

Isolate: test one New at a time on top of a faithful Proven base, so the result means
something.

**Split the risks.** Most ideas carry several independent risks. Give each its own probe:

- **Demand**: will people want it and come back?
- **Supply / content**: will enough people contribute, rate, post, list or host? Most
  users never contribute, so this is often the real killer for ratings, marketplaces and
  UGC.
- **Distribution**: can you reach the audience cheaply and repeatedly?
- **Monetization**: will anyone pay, and how much?

A single combined test that fails can't tell you which risk killed it.

**What counts as a test.** Interviews and data cuts are research that sharpens the
hypotheses. Experiments are probes where real users act. Thresholds and kill rules
apply to experiments. For research, state the question it must answer and the decision
it feeds.

## 5. Reading the result

- **Heat is obvious.** Numbers repeat when you rerun, users ask for more, they share it
  without being asked, they complain when it's taken away. Pincus turned a link on for
  one minute, got the same click rate twice, and took that as enough.
- **Lukewarm is a no.** "Some people liked it" is the B+ zone. Don't rationalize.
- **Watch for false positives**: mechanics that lift anything (rewards, scarcity, free
  stuff), novelty that fades in a week, friends being polite, a small sample of fans.
- **Read why it failed.** Did the New fail, or did the proven base get broken and drag
  it down? Fail for the right reason.
- **Kill quickly.** One team (Twitch's founders, pre-Twitch) killed any idea that didn't
  show results within about a week. If you must choose between the *most* shots and the
  *best* shots, most usually wins, because nobody knows in advance which shot is best.
  Twitchiness is a strength when it's anchored to one vision.

## 6. Failure machines and AI

Since most New ideas fail, build a **failure machine**: a system where the marginal cost
of testing an idea is close to zero, so you can test more ideas in a week than the
industry tests in a year. At Zynga that meant links and pop-ups in live games, and
eventually internal ad-serving technology that could test hundreds of ideas a day.

AI makes this cheaper than ever, but Pincus's worry is that teams use it to build one
idea faster instead of testing a hundred. Use it as a testing machine:

- Generate many variants (copy, art, onboarding flows, feature concepts) and test them
  against real users in parallel through ads, fake doors or prototypes.
- Vibe-code throwaway prototypes in hours rather than polishing one in months.
- Use simulated users only to filter options before real tests. Simulation is not
  signal.
- Keep the human job: taste, empathy, and spotting which result is true signal.

## 7. From signal to a Maximum Launch Product

The point of a cheap test is to earn conviction. Once you have true signal:

- **Overinvest** in the winning idea. Build it properly: the hacky Bold Beat becomes a
  real system. (FarmVille's crafting buildings were shipped as a hack in a month, then
  rebuilt over six months into the game's biggest engagement driver.)
- **Launch big**, as a Maximum Launch Product rather than a timid MVP, because you
  already know it's a hit. Makers who test this way (Brian Chesky is the book's example)
  don't launch to find out whether people like it.
- Being in market with real users makes a team far more creatively productive than
  polishing in private. Teams that keep saying "it's not ready, we haven't found the
  fun" usually need to put something rough in front of users now.

## 8. Cautionary cases

- **Quibi**: a right instinct (short video on phones) bet entirely on one expensive idea
  (premium Hollywood shows) without cheap tests. It shut down within months. Cheap,
  addictive serialized short dramas later proved the instinct at scale.
- **Words With Friends "Fast Play"**: a team assumed the game was too slow and spent six
  months building a faster mode. Few players tried it and almost none returned; the core
  audience loved the slow, turn-based rhythm. A dialog-box test would have shown this in
  an hour. The winning idea, weekly challenges, was tested as a simple progress bar
  first, and helped turn the franchise around.
- **Tribe.net** (Pincus's own): strong invite numbers hid weak retention. He stuck with
  one idea instead of testing alternatives and going with whatever had the most heat.
