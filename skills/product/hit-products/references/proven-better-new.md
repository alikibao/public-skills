# Proven Better New

Pincus's central framework, the "religion" of Zynga's product management. Wording and
examples here are a distillation, not quotes.

## Contents
1. The three parts
2. Why it works, and why people resist it
3. How to do Proven properly
4. How to test Better
5. How to handle New
6. How much New you need depends on the water
7. Worked examples
8. Pitfalls
9. Teardown template

## 1. The three parts

- **= Proven.** An experience the target audience already loves, *on this platform*,
  broken down to the specific mechanics, flows and details (down to the pixel). You
  reuse it, legally and with taste, so the product doesn't fail for the wrong reasons.
- **> Better.** Improvements to the proven experience that 10 out of 10 of its current
  users would enthusiastically call better. It's objective, not your opinion: free
  instead of paid, no download, half the price, fewer steps, works where they already
  are, polish on the core loop. Better is usually small, and rarely wins alone except
  during a platform shift.
- **+ New.** The novel idea that has never been tried with this product and audience.
  It's the reason to try the product and talk about it, and it's the most likely part to
  fail. Pincus's maxim was that "all New fails". That isn't meant to discourage
  invention. It means isolating it, testing it, and having other News ready.

The trap that catches almost everyone: **what the maker thinks is Better is actually
New.** If you can't honestly say every existing user would agree, it's New, and it
needs to be tested.

## 2. Why it works, and why people resist it

Consumer success is close to unpredictable. Starting from something with proven heat
changes the odds. When you rebuild the proven experience faithfully, you avoid the
false negatives that come from getting basic things wrong. One story from the book: a
legendary game designer launched a social game whose first-time experience took too
many clicks, so almost nobody ever reached the brilliant design underneath. Junior
product managers who had studied the proven onboarding spotted it within minutes.

Isolating New also gives clean signal. If you change ten things and it fails, you learn
nothing. If you copy the proven base and change one thing, the result tells you about
that one thing.

People resist because of a **moral arbitrage**. Copying feels like cheating, and makers
want to be innovators, respected by peers. Junior teams spend real effort trying *not*
to look like a copy. That reluctance is exactly why the opportunity stays open for
people with less ego involved. Masters copy well: they can see excellence, understand
that changing it would make it worse, and save their originality for where it counts.
Users don't care whether you were original. They care whether it's one inch better for
them. The best copies are done with enough taste that nobody notices what they came from.

Copying alone gives users no reason to switch, which is why Better and New exist.

## 3. How to do Proven properly

**Get a PhD in the proven before you earn the right to innovate.** Before changing the
camera, onboarding or feed, become the world's leading expert on the best existing
versions.

- **Be precise about "proven".** It means: on this platform, for this audience, for this
  experience. A game that was popular in the 1990s on PC is not proven for mobile
  casual players today. A behavior inside Roblox is only fuzzily proven on the web.
  Founders often misuse the word to justify an idea they already have.
- **Deconstruct to the atomic unit.** List every mechanic, step, screen, default and
  piece of copy in the proven product. A useful mental model is the slot machine: it's an
  interface plus tuning, and an identical copy should produce the identical response.
  If you can't rebuild it and expect the same reaction, you haven't understood it yet.
- **Don't change what you don't understand.** At Zynga, a designer removed what looked
  like pointless friction from a farm game: an empty friends bar that pushed players to
  send invitations. The team kept it, because nobody yet understood why it worked. It
  turned out to drive invitations, virality and reminders to come back. Change proven
  details later, behind a test.
- **Measure heat.** Nikita Bier (tbh, Gas, later head of product at X) frames heat as
  *frequency × intensity*: how often people do it and how much they care each time.
  Snapchat turned photos into something people did dozens of times a day.
- **Hunt latent demand.** The most valuable proven thing is often a feature that's
  generating so much heat that users put up with a bad product to get it: an app with
  a store page in the wrong language that still tops the charts, or a ritual people run
  by hand through screenshots. Build the product those users actually want.
- **Copy proven pieces from anywhere for everything that isn't your New**: onboarding
  from whoever converts best, contact sync from the incumbents, notification patterns
  from the stickiest apps. Keep a running inventory of best-of-breed flows.
- **Benchmark the ecosystem continuously.** Being first matters less than being best:
  Zynga's mantra was best to market, not first to market. Whenever a competitor gets
  better growth or engagement, take apart which mechanics did it, match them, then
  innovate on top (FarmVille launched as Proven + Better against the leading farm game,
  then out-innovated it within weeks).
- **Copy yourself.** Inside a company, a mechanic that works in one product should
  spread to the others within days. Nobody minds copying their own team.

## 4. How to test Better

For each proposed Better item, ask:

1. Who are the current users of the proven product? (Not you, not your team.)
2. Would every one of them say yes, that's better, without needing an explanation?
3. Can you show it statistically, or is it a matter of taste?

Start with the **ask**: everything the product requires before it pays off. That means
money, a download, an account, setup, minutes per session, learning new rules, and
getting friends to join. Pincus found that requiring a download loses most of an
audience. His recipe for making games mass-market was a game people already knew,
free, about three clicks to start, and 5–15 minutes a session, placed where people
would stumble on it. Every cut to the ask is a genuine Better.

Typical genuine Betters: price (free, cheaper), access (no download, instant play,
works inside the platform they already use), speed, fewer clicks on the core loop, a
cleaner and less noisy interface, a faster first-time experience, mobile or touch polish,
importing an existing graph so the product isn't empty on day one.

Typical fake Betters, which are really New: "more social", "AI-powered", a new
organizing concept, a different feed algorithm, a redesigned navigation, a faster or
shorter version of the core activity. (Zynga once spent six months building a faster
version of a word game. Its core audience loved the unhurried, turn-based pace and
never adopted it.)

Users also feel ownership of products they rely on. They move fast through them by
habit and get angry at change, even change for the better. A master like Craigslist's
founder reportedly took around two years to add photos to listings, because he cared
about not breaking what people relied on. When the proven base is already loved,
Better should be cautious polish.

## 5. How to handle New

- **Expect it to fail**, and prosecute it like a scientist: isolate it, give it a
  clean test, judge it on a threshold you set beforehand (see `testing.md`).
- **Keep it narrow.** The best New is often one thing. Zynga Poker's only New was
  showing real people with their real profile photos at the table, which made it a
  live cocktail party instead of a game with creepy avatars.
- **Have more than one ready.** If you go in assuming New #1 fails and New #2–#5 are
  lined up, you run the work differently and much faster.
- **New gets people to try; Proven and Better keep them.** New is the back-of-the-box
  line, the thing that makes someone download it or talk about it.
- **Sources of good New:** a new dimension added to a tired activity (social identity on
  poker; a cultural lens on a soap-opera format); a feature that's buried in someone
  else's product, pulled out and made the whole product; a new platform capability; a
  piece of trust or identity infrastructure that suddenly exists.
- **The best case needs no New at all.** If Proven + Better is enough (it often is on a
  new platform), take the win. People don't like change.

## 6. How much New you need depends on the water

| Context | What works | Why |
|---|---|---|
| **Platform shift** (web → social → mobile → AI) | Proven + Better, little or no New. **The platform is the New.** | Users are in discovery mode, acquisition is cheap or viral, and incumbents are slow to move. FarmVille-style games moved to mobile; Call of Duty overtook its rival on a new console generation; AI-native startups reach large revenue in sleepy verticals. |
| **Mature market** (red ocean) | A lot of New, an "OMFG" level reason to switch | Everyone is committed to existing services and nobody is in discovery mode. But mature markets are also where incumbents stopped innovating. Reinventing the core value can turn an "over" market back into a growth market (search before Google, games before social games). |
| **New planet** (nothing proven on this platform yet) | **Fuzzy Proven**: the atomic behavior that's proven elsewhere, made native | See `new-platforms.md`. Uber kept the atomic unit "a paid ride from A to B", made booking and status Better through the phone and map, and the New was that anyone could be the driver. |

Risk/return view (Pincus's two-by-two for his students): pure New with no Proven is
**wildcat drilling**. It's high-risk, and the occasional gusher (a studio's 45th
completely different attempt finally hitting) isn't repeatable. Relying on licensed
proven IP is low-risk but the IP owner takes the margin. Proven Better New is the
quadrant with high odds *and* high margin.

## 7. Worked examples

Brief, paraphrased summaries of cases from the book and interview:

| Product | Proven | Better | New |
|---|---|---|---|
| **Zynga Poker** (2007) | Standard online poker table layout and rules | Free, instant play in the browser, no download (downloads lose most of an audience) | Real people, often friends, with real profile photos at the table |
| **FarmVille** (2009) | The viral farm-game formula already working on Facebook (free-form plot, avatar, friends bar) | Better crop art and economy, fewer clicks (tool attached to the cursor), first game to use the newly opened news feed | Effectively none at launch. Novel features (moving animals, buildings with gameplay) came weeks later as tests |
| **Hay Day** (Supercell) | FarmVille, faithfully, down to the driveway, mailbox and pickup truck | Rebuilt for mobile: shorter crop timers, simpler menus, tactile touch farming | Little: a masterclass in Proven + Better on a new platform |
| **Slack** | HipChat-style team chat used by engineers | Friendlier, more fun interface that end users loved | Hardly any at first. Spread through teams, not IT departments |
| **tbh** (Nikita Bier) | Teens' viral demand for positive anonymous feedback (a top-charting app with a clunky interface; compliment screenshots shared on Snapchat) | A clean, English-language form factor; contact sync and onboarding copied from the best converters | Pre-written positive polls plus a hint about who voted ("a 9th-grade girl"), which made results screenshot-worthy and drove the viral loop |
| **Threads** (AI-assisted teardown in the book) | Twitter-style feed, replies, reposts; Instagram profile and stories layout | Instant onboarding by importing an Instagram identity and follows; cleaner feed with no ads at first | Piggybacking an existing social graph into a new app at scale; cross-app notification loops |
| **Words With Friends** | Scrabble | Polished for mobile, asynchronous, free | Friends from your social graph already there to play |
| **Empire** (TV) | The soap-opera family power-struggle format | Contemporary music-industry setting | A cultural lens: centered on Black protagonists, an audience underserved by the format |
| **Draw Something** (OMGPOP) | Pictionary, plus Words With Friends' turn-based social system copied exactly | Mobile-native | The drawing-and-guessing twist on the turn-based format. The studio had already failed with something entirely new; this time it went proven-first out of desperation and reached #1 |

Contrast: **Zynga Poker 2.0** (2014) was all New with no Proven. Loyal players revolted,
a distant competitor doubled its users, and Zynga restored the classic version, which
then outperformed the new one.

## 8. Pitfalls

- **Fake Proven**: proven somewhere else, for someone else, at another time.
- **Better that is really New**, so untested risk hides inside the "safe" column.
- **Too much New**: reinventing everything makes the product wide, shallow and
  confusing, and when it fails you don't know why.
- **Changing the proven base** before understanding why it works.
- **PBN as a crutch**: copying a successful base produces decent early numbers, so a
  weak New can coast to a B+ and never become an A. Judge the New on its own signal.
- **AI homogenization**: a model can produce a competent PBN analysis in seconds, and
  the result will tend toward the average. In the book's own test, the model did well on
  Proven, mislabelled New ideas as Better, and produced conventional New ideas. Use AI to
  deconstruct and to generate options. Real users decide.
- **Magic the user didn't ask for**: delightful to the maker, irrelevant at the user's
  moment of need (see the "Pincus Problem" in `principles.md`).
- **Magic still matters.** Sometimes a team should build something purely for quality
  and delight (Airbnb's one-off "Icons" stays are the book's example). Treat it as R&D,
  and know you're doing it.

## 9. Teardown template

Use this for a hit, a competitor, or the proven product a new idea builds on.

```
## Teardown: <product>

Audience and platform: <who exactly, where, when it launched>
Context: <platform shift / mature market / new planet>, and why the timing worked

Core loop: <the repeated action and its payoff>
Heat: frequency <how often> × intensity <how much users care>; evidence: <metrics, rankings, reviews, behavior>

= Proven (what it reused, and from where)
- <mechanic / flow / detail> — from <source product>
...

> Better (what it improved that 10/10 users of the source would agree on)
- <improvement> — why it's objectively better
...

+ New (what was novel for this audience and platform)
- <novel element> — the risk it took; how it could have been tested cheaply

Distribution: <how it reached people: platform hack, graph import, viral loop, breadcrumbs>
Retention engine: <why people return; the leading metric you'd guess they watch>
What didn't work / what changed later: <...>

Lessons for <user's product>: <what to copy exactly, what to make better, where to put your New>
```

When researching, cite sources and separate facts you verified from inferences.
