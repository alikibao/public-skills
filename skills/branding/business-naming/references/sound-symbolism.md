# Sound symbolism and processing fluency

These are tendencies from sound-symbolism research (bouba/kiki, mil/mal-style studies,
brand-name experiments) and from naming-agency practice. They are probabilities, not
laws. Use them to **steer** a promising name toward the desired feel and to **break
ties** — never to veto a name that has meaning and energy.

## Processing fluency

- **Consonant–vowel rhythm** (CVCV…) is the earliest pattern children produce (ma-ma,
  da-da) and travels easily across languages: Sonos, Toyota, Lego, Nokia.
- **Two or three syllables** is the sweet spot. One syllable works best when it's a real
  word; four or more needs a strong rhythm (Im-pos-si-ble works because it's a word).
- **Clusters** of three or more consonants slow non-native speakers.
- **Real words and familiar morphemes** process fastest. Let the surprise come from the
  context, not from difficulty.
- **Hear it, spell it.** Avoid spellings with several options for one sound (c/k, ph/f,
  ee/ea/ie, y/i) unless the word is already known. Every respelling taxes word of mouth
  and search.
- **Repetition and echo** (Sonos, Coca-Cola, Kit Kat) help memory.

## What sounds tend to signal

| Sounds | Tends to feel | Notes |
|---|---|---|
| Voiceless stops **p, t, k** | fast, sharp, precise, small | Punchy openers; K reads powerful |
| Voiced stops **b, d, g** | sturdy, reliable, bigger | The agency found **B** one of the most reliable sounds across languages (BlackBerry) |
| **z**, **x** | speed, edge, energy | **X** reliably signals innovation/tech (SpaceX, Lexus, Xeon) — so it's surprising only outside tech |
| Fricatives **f, v, s, sh, h, th** | airy, smooth, soft, light, fresh | Lightness and freshness: Feather, Febreze, Swiffer |
| Nasals **m, n** | warm, comforting, human | m recalls comfort and care |
| Liquids **l, r** | flowing, smooth, gentle | l feels light; r adds movement |
| Front vowels **i** (bee), **e** | small, light, quick, bright | "mil" is judged smaller than "mal" |
| Back/open vowels **o, u, a** | big, round, heavy, slow, warm, deep | "bouba" is round, "kiki" is spiky |

## Matching a desired feel

- **Fast / agile:** voiceless stops, z, x, front vowels, short words.
- **Reliable / solid:** b, d, g, k, balanced CV rhythm, back vowels.
- **Light / fresh:** f, s, sh, l, front vowels, open endings.
- **Warm / human:** m, n, l, open vowels, soft endings.
- **Premium / calm:** fewer stops, longer vowels, liquids and nasals.

## Using the script

```
python <skill-dir>/scripts/name_tools.py phonetics Feather Updraft Pentium --profile light fast
python <skill-dir>/scripts/name_tools.py phonetics --from shortlist.json --profile reliable warm
```

Profile words it understands include: fast, quick, light, fresh, sharp, crisp, strong,
bold, reliable, trusted, solid, big, premium, smooth, soft, calm, elegant, warm, friendly,
human, edgy, innovative, modern.

It reports syllables, the C/V pattern, alternation (1.0 = perfect CVCV), the longest
consonant cluster, spelling traps, a structural *ease* score, the strongest *feels*, and
*fit* against the requested profile. It reads spelling, not sound — always say the name
out loud before trusting a number.
