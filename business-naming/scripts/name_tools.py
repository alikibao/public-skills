#!/usr/bin/env python3
"""Helper commands for the business-naming skill.

Commands
  check      Validate a naming team's JSONL output file.
  merge      Combine team JSONL files, dedupe, and print the "sonar" readout
             (per-team and per-territory yield, favourites, cross-team collisions).
  phonetics  Heuristic structure + sound-symbolism readout for candidate names.
  sparks     Draw random "unfamiliar magazines" (far domains) for synchronicity.
  handles    List domain and social-handle variants worth checking.

Examples
  python name_tools.py check work/04-dream/c1/team-a.jsonl
  python name_tools.py merge "work/04-dream/**/*.jsonl" --out work/05-judging/merged.json
  python name_tools.py phonetics Feather Swiffer Pentium --profile light fast
  python name_tools.py phonetics --from work/05-judging/shortlist.json --profile reliable
  python name_tools.py sparks --n 4
  python name_tools.py handles Feather Lumen --cc za

Everything here is a heuristic aid for human-style judgement. The phonetics
readout works from spelling, not pronunciation, and English spelling is loose.
"""

import argparse
import glob
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path


# --------------------------------------------------------------------------
# shared helpers
# --------------------------------------------------------------------------

def norm_key(name: str) -> str:
    """Case/punctuation-insensitive key used for dedupe."""
    return re.sub(r"[^a-z0-9]", "", name.lower())


def slug(name: str) -> str:
    return norm_key(name)


def expand_paths(patterns):
    paths = []
    for pat in patterns:
        hits = sorted(glob.glob(pat, recursive=True))
        if hits:
            paths.extend(hits)
        elif Path(pat).exists():
            paths.append(pat)
        else:
            print(f"warning: no files match {pat}", file=sys.stderr)
    seen, out = set(), []
    for p in paths:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def read_jsonl(path):
    """Yield (line_no, obj or None, error or None)."""
    with open(path, encoding="utf-8") as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                yield i, None, f"invalid JSON ({exc.msg})"
                continue
            if not isinstance(obj, dict):
                yield i, None, "line is not a JSON object"
                continue
            yield i, obj, None


def cycle_from_path(path: str) -> str:
    m = re.search(r"(?:^|[\\/])(c\d+|cycle[-_]?\d+)(?:[\\/]|$)", path)
    return m.group(1) if m else ""


def team_from_path(path: str) -> str:
    m = re.search(r"team[-_]?([a-z0-9]+)", Path(path).stem, re.I)
    return m.group(1).upper() if m else ""


# --------------------------------------------------------------------------
# check
# --------------------------------------------------------------------------

def cmd_check(args):
    ok = True
    for path in expand_paths(args.files):
        errors, warnings = [], []
        names = Counter()
        favs = 0
        total = 0
        for line_no, obj, err in read_jsonl(path):
            if err:
                errors.append(f"line {line_no}: {err}")
                continue
            total += 1
            name = obj.get("name")
            if not isinstance(name, str) or not name.strip():
                errors.append(f"line {line_no}: missing or empty 'name'")
                continue
            names[norm_key(name)] += 1
            if not obj.get("territory"):
                warnings.append(f"line {line_no}: no 'territory' for {name!r}")
            if obj.get("favorite") is True:
                favs += 1
        dupes = [k for k, c in names.items() if c > 1]
        print(f"{path}: {total} lines, {len(names)} unique names, {favs} favourites")
        if dupes:
            print(f"  note: {len(dupes)} names repeated within this file "
                  f"(e.g. {', '.join(dupes[:5])})")
        for w in warnings[:5]:
            print(f"  warning: {w}")
        if len(warnings) > 5:
            print(f"  ... {len(warnings) - 5} more warnings")
        for e in errors[:10]:
            print(f"  ERROR: {e}")
        if errors:
            ok = False
            print(f"  {len(errors)} error(s) — fix before merging")
    return 0 if ok else 1


# --------------------------------------------------------------------------
# merge
# --------------------------------------------------------------------------

def cmd_merge(args):
    paths = expand_paths(args.files)
    if not paths:
        print("no input files", file=sys.stderr)
        return 1

    entries = {}
    order = []
    team_total = Counter()
    team_favs = Counter()
    terr_total = Counter()
    terr_favs = Counter()
    bad_lines = 0
    raw_lines = 0

    for path in paths:
        default_team = team_from_path(path)
        cycle = cycle_from_path(path)
        for _, obj, err in read_jsonl(path):
            if err or not isinstance(obj.get("name"), str) or not obj["name"].strip():
                bad_lines += 1
                continue
            raw_lines += 1
            name = obj["name"].strip()
            key = norm_key(name)
            if not key:
                bad_lines += 1
                continue
            team = str(obj.get("team") or default_team or "?").upper()
            territory = str(obj.get("territory") or "unspecified").strip()
            fav = obj.get("favorite") is True
            team_total[team] += 1
            terr_total[territory.lower()] += 1
            if fav:
                team_favs[team] += 1
                terr_favs[territory.lower()] += 1

            if key not in entries:
                entries[key] = {
                    "name": name,
                    "key": key,
                    "teams": set(),
                    "territories": set(),
                    "moves": set(),
                    "sparks": [],
                    "favorite_by": set(),
                    "cycles": set(),
                    "hits": 0,
                }
                order.append(key)
            e = entries[key]
            e["hits"] += 1
            e["teams"].add(team)
            e["territories"].add(territory)
            if obj.get("move"):
                e["moves"].add(str(obj["move"]))
            spark = obj.get("spark")
            if spark and len(e["sparks"]) < 3 and spark not in e["sparks"]:
                e["sparks"].append(str(spark))
            if fav:
                e["favorite_by"].add(team)
            if cycle:
                e["cycles"].add(cycle)

    names_out = []
    for key in order:
        e = entries[key]
        names_out.append({
            "name": e["name"],
            "teams": sorted(e["teams"]),
            "territories": sorted(e["territories"]),
            "moves": sorted(e["moves"]),
            "sparks": e["sparks"],
            "favorite": bool(e["favorite_by"]),
            "favorite_by": sorted(e["favorite_by"]),
            "cycles": sorted(e["cycles"]),
        })

    collisions = [n for n in names_out if len(n["teams"]) > 1]

    # Territory "sonar": yield and favourite rate per territory.
    terr_rows = []
    for terr, total in terr_total.most_common():
        favs = terr_favs.get(terr, 0)
        terr_rows.append({"territory": terr, "names": total, "favorites": favs,
                          "favorite_rate": round(favs / total, 3) if total else 0})

    stats = {
        "files": paths,
        "lines_read": raw_lines,
        "bad_lines": bad_lines,
        "unique_names": len(names_out),
        "per_team": {t: {"names": team_total[t], "favorites": team_favs.get(t, 0)}
                     for t in sorted(team_total)},
        "territories": terr_rows,
        "cross_team_collisions": [c["name"] for c in collisions],
    }

    if args.out:
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump({"stats": stats, "names": names_out}, fh, indent=1, ensure_ascii=False)

    # Human readout
    print(f"Merged {len(paths)} file(s): {raw_lines} lines -> {len(names_out)} unique names"
          + (f" ({bad_lines} bad lines skipped)" if bad_lines else ""))
    print("\nPer team (names / favourites):")
    for t in sorted(team_total):
        print(f"  Team {t}: {team_total[t]} / {team_favs.get(t, 0)}")
    print("\nTerritory sonar (names, favourites, favourite rate) — high rate = a vein worth diving on:")
    rich = sorted(terr_rows, key=lambda r: (r["favorites"], r["favorite_rate"]), reverse=True)
    for r in rich[: args.top]:
        print(f"  {r['territory'][:40]:40s} {r['names']:4d}  {r['favorites']:3d}  {r['favorite_rate']:.0%}")
    if len(rich) > args.top:
        print(f"  ... {len(rich) - args.top} more territories in the JSON")
    dry = [r for r in terr_rows if r["names"] >= 8 and r["favorites"] == 0]
    if dry:
        print("\nDry territories (8+ names, no favourites): "
              + ", ".join(r["territory"] for r in dry[:12]))
    if collisions:
        print(f"\nCross-team collisions ({len(collisions)}) — independent teams reached the same name;"
              " often a sign it is the obvious move, so treat as a warning, not a win:")
        print("  " + ", ".join(c["name"] for c in collisions[:30]))
    if args.out:
        print(f"\nWrote {args.out}")
    return 0


# --------------------------------------------------------------------------
# phonetics
# --------------------------------------------------------------------------

VOWELS = set("aeiou")
FRONT_VOWELS = set("ie")
BACK_VOWELS = set("ou")

# token class -> set of tags
CLASS_TAGS = {
    "vstop": {"stop", "voiceless"},       # p t k
    "dstop": {"stop", "voiced"},          # b d g
    "fric": {"fric"},                     # f v s z h sh th ph
    "affr": {"affr"},                     # ch j
    "nasal": {"nasal"},                   # m n ng
    "liquid": {"liquid"},                 # l r
    "glide": {"glide"},                   # w y
    "x": {"stop", "voiceless", "fric", "x"},  # x ~ ks
}

SINGLE = {
    "p": "vstop", "t": "vstop", "k": "vstop", "q": "vstop",
    "b": "dstop", "d": "dstop", "g": "dstop",
    "f": "fric", "v": "fric", "s": "fric", "z": "fric", "h": "fric",
    "j": "affr",
    "m": "nasal", "n": "nasal",
    "l": "liquid", "r": "liquid",
    "w": "glide",
    "x": "x",
}
DIGRAPHS = {"sh": "fric", "th": "fric", "ph": "fric", "ch": "affr", "ck": "vstop",
            "ng": "nasal", "qu": "vstop", "wh": "glide", "gh": "fric"}


def tokenize(word: str):
    """Very rough letter-to-sound-class tokenizer.

    Returns a list of (kind, letters, cls) where kind is 'C' or 'V'.
    """
    w = re.sub(r"[^a-z]", "", word.lower())
    toks = []
    i = 0
    n = len(w)
    while i < n:
        ch = w[i]
        pair = w[i:i + 2]
        # silent final e: consonant + e at the end of words longer than 3 letters
        if ch == "e" and i == n - 1 and n > 3 and toks and toks[-1][0] == "C" \
                and not (n >= 2 and w[i - 1] == "l" and n >= 3 and w[i - 2] not in VOWELS):
            break
        if ch in VOWELS:
            j = i
            while j < n and w[j] in VOWELS:
                j += 1
            toks.append(("V", w[i:j], "vowel"))
            i = j
            continue
        if ch == "y":
            # consonant at word start or before a vowel, vowel otherwise
            if i == 0 or (i + 1 < n and w[i + 1] in VOWELS):
                toks.append(("C", "y", "glide"))
            else:
                toks.append(("V", "y", "vowel"))
            i += 1
            continue
        if ch == w[i + 1:i + 2] and ch not in VOWELS:
            # doubled consonant (ff, ss, rr) is one sound
            toks.append(("C", ch * 2, SINGLE.get(ch, "vstop" if ch == "c" else "other")))
            i += 2
            continue
        if pair in DIGRAPHS:
            toks.append(("C", pair, DIGRAPHS[pair]))
            i += 2
            continue
        if ch == "c":
            nxt = w[i + 1] if i + 1 < n else ""
            toks.append(("C", "c", "fric" if nxt in ("e", "i", "y") else "vstop"))
            i += 1
            continue
        toks.append(("C", ch, SINGLE.get(ch, "other")))
        i += 1
    return toks


def split_parts(name: str):
    parts = re.split(r"[\s\-_.]+", name.strip())
    out = []
    for p in parts:
        # split camelCase / PascalCase compounds: HubSpot -> Hub, Spot
        out.extend([x for x in re.findall(r"[A-Z]?[a-z]+|[A-Z]+(?![a-z])|\d+", p) if x])
    return out or [name]


def analyse(name: str):
    parts = split_parts(name)
    all_toks = []
    for p in parts:
        all_toks.extend(tokenize(p))
    letters = re.sub(r"[^a-z]", "", name.lower())

    pattern = "".join(t[0] for t in all_toks)
    syllables = max(1, sum(1 for t in all_toks if t[0] == "V"))

    # alternation: share of adjacent token pairs that switch C<->V
    if len(pattern) > 1:
        switches = sum(1 for a, b in zip(pattern, pattern[1:]) if a != b)
        alternation = switches / (len(pattern) - 1)
    else:
        alternation = 1.0
    clusters = re.findall(r"C+", pattern)
    max_cluster = max((len(c) for c in clusters), default=0)

    # spelling-from-hearing ambiguity flags
    flags = []
    low = name.lower()
    checks = [
        (r"ph", "ph/f"), (r"gh", "gh"), (r"ough", "ough"), (r"^kn|^wr|^ps|^pn", "silent first letter"),
        (r"ei|ie", "ei/ie"), (r"c[eiy]", "soft c"), (r"q(?!u)", "q without u"),
        (r"^x", "initial x (z or ks?)"), (r"[a-z]y[bcdfghjklmnpqrstvwxz]", "y as vowel"),
        (r"ae|oe", "ae/oe"), (r"\d", "digit"), (r"([a-z])\1\1", "triple letter"),
        (r"ee|ea", "ee/ea"), (r"k[aeiou]|c[aou]", None),
    ]
    for pat, label in checks:
        if label and re.search(pat, low):
            flags.append(label)
    # both c and k spelling options exist for a hard /k/ at the start
    if re.match(r"^[ck][aou]", low):
        flags.append("c/k start")

    # sound-symbolism tallies per token
    dims = Counter()
    ntok = max(1, len(all_toks))
    for kind, lets, cls in all_toks:
        if kind == "V":
            first = lets[0]
            if first in FRONT_VOWELS or lets == "y":
                dims["fast"] += 0.7
                dims["light"] += 1.0
                dims["sharp"] += 0.8
            elif first in BACK_VOWELS:
                dims["big"] += 1.0
                dims["smooth"] += 0.5
                dims["warm"] += 0.5
            else:  # a
                dims["big"] += 0.6
                dims["warm"] += 0.6
            continue
        tags = CLASS_TAGS.get(cls, set())
        if "stop" in tags:
            dims["strong"] += 1.0
            if "voiceless" in tags:
                dims["fast"] += 1.0
                dims["sharp"] += 1.0
            if "voiced" in tags:
                dims["big"] += 0.7
                dims["reliable"] += 1.0
        if "fric" in tags:
            dims["light"] += 0.9
            dims["fast"] += 0.6
            dims["smooth"] += 0.4
        if lets in ("z", "x"):
            dims["fast"] += 0.8
            dims["edge"] += 1.0
        if lets == "b":
            dims["reliable"] += 0.5
        if lets == "k" or (lets == "c" and cls == "vstop") or lets == "ck":
            dims["strong"] += 0.4
        if "affr" in tags:
            dims["strong"] += 0.5
            dims["edge"] += 0.4
        if "nasal" in tags:
            dims["warm"] += 1.0
            dims["smooth"] += 0.8
        if "liquid" in tags:
            dims["smooth"] += 1.0
            dims["light"] += 0.3
        if "glide" in tags:
            dims["smooth"] += 0.6
            dims["light"] += 0.4

    # normalise to a 0-10 scale relative to token count (cap at 10)
    profile = {k: round(min(10.0, v / ntok * 12), 1) for k, v in dims.items()}

    # structure ease heuristic (0-10)
    ease = 10.0
    if syllables > 3:
        ease -= 1.2 * (syllables - 3)
    if syllables == 1 and len(letters) > 6:
        ease -= 1.0
    ease -= max(0, max_cluster - 2) * 1.5
    ease -= (1 - alternation) * 3
    ease -= 0.7 * len([f for f in flags if f not in ("c/k start",)])
    ease -= 0.4 * len([f for f in flags if f == "c/k start"])
    if len(letters) > 10:
        ease -= 0.5 * (len(letters) - 10)
    ease = round(max(0.0, min(10.0, ease)), 1)

    # echo / repetition (memorability aids)
    echoes = []
    if len(parts) > 1:
        initials = [p[0].lower() for p in parts if p]
        if len(set(initials)) < len(initials):
            echoes.append("alliteration")
        ends = [p[-2:].lower() for p in parts if len(p) >= 2]
        if len(set(ends)) < len(ends):
            echoes.append("rhyme")
    cons = [t[1] for t in all_toks if t[0] == "C"]
    rep = [c for c, k in Counter(cons).items() if k > 1]
    if rep:
        echoes.append("repeated " + "/".join(sorted(rep)))
    if re.match(r"^(?:cv)+c?$", pattern.lower()) and len(pattern) >= 4:
        echoes.append("CV rhythm")

    top = sorted(profile.items(), key=lambda kv: kv[1], reverse=True)[:3]
    return {
        "name": name,
        "letters": len(letters),
        "syllables": syllables,
        "pattern": pattern,
        "alternation": round(alternation, 2),
        "max_cluster": max_cluster,
        "spelling_flags": flags,
        "ease": ease,
        "echoes": echoes,
        "profile": profile,
        "top_feel": [k for k, _ in top],
    }


PROFILE_SYNONYMS = {
    "fast": "fast", "quick": "fast", "speed": "fast", "speedy": "fast", "agile": "fast", "nimble": "fast",
    "light": "light", "lightweight": "light", "airy": "light", "fresh": "light", "small": "light",
    "delicate": "light", "precise": "sharp",
    "sharp": "sharp", "crisp": "sharp", "bright": "sharp", "clever": "sharp", "smart": "sharp",
    "strong": "strong", "powerful": "strong", "power": "strong", "bold": "strong", "punchy": "strong",
    "reliable": "reliable", "trust": "reliable", "trusted": "reliable", "dependable": "reliable",
    "solid": "reliable", "sturdy": "reliable", "safe": "reliable",
    "big": "big", "large": "big", "heavy": "big", "substantial": "big", "premium": "big", "deep": "big",
    "smooth": "smooth", "soft": "smooth", "gentle": "smooth", "calm": "smooth", "flowing": "smooth",
    "elegant": "smooth", "luxurious": "smooth",
    "warm": "warm", "friendly": "warm", "caring": "warm", "human": "warm", "comfort": "warm",
    "edgy": "edge", "edge": "edge", "innovative": "edge", "tech": "edge", "futuristic": "edge",
    "modern": "edge",
}


def load_names_from_json(path):
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    if isinstance(data, dict):
        for key in ("names", "shortlist", "finalists", "candidates"):
            if isinstance(data.get(key), list):
                data = data[key]
                break
    out = []
    if isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                out.append(item)
            elif isinstance(item, dict) and isinstance(item.get("name"), str):
                out.append(item["name"])
    return out


def cmd_phonetics(args):
    names = list(args.names)
    if args.from_file:
        names.extend(load_names_from_json(args.from_file))
    if not names:
        print("give names as arguments or --from a JSON file", file=sys.stderr)
        return 1

    wanted, unknown = [], []
    for word in args.profile or []:
        dim = PROFILE_SYNONYMS.get(word.lower())
        if dim and dim not in wanted:
            wanted.append(dim)
        elif not dim:
            unknown.append(word)
    if unknown:
        print(f"note: profile words not recognised (ignored): {', '.join(unknown)}", file=sys.stderr)

    rows = []
    for n in names:
        r = analyse(n)
        if wanted:
            r["fit"] = round(sum(r["profile"].get(d, 0) for d in wanted) / len(wanted), 1)
        rows.append(r)

    if args.json:
        print(json.dumps(rows, indent=1, ensure_ascii=False))
        return 0

    if wanted:
        rows.sort(key=lambda r: r["fit"], reverse=True)
        print(f"Sorted by fit to desired feel: {', '.join(wanted)}\n")
    head = "| name | syl | pattern | alt | max cl | ease | feels | echoes | spelling flags |"
    if wanted:
        head = head + " fit |"
    print(head)
    print("|" + "---|" * (head.count("|") - 1))
    for r in rows:
        line = (f"| {r['name']} | {r['syllables']} | {r['pattern']} | {r['alternation']:.2f} | "
                f"{r['max_cluster']} | {r['ease']} | {', '.join(r['top_feel'])} | "
                f"{'; '.join(r['echoes']) or '-'} | {'; '.join(r['spelling_flags']) or '-'} |")
        if wanted:
            line += f" {r['fit']} |"
        print(line)
    print("\nease = structural ease from spelling (syllables, C/V alternation, clusters, spelling traps); "
          "feels = strongest sound-symbolism tendencies. Heuristic only — say each name aloud.")
    return 0


# --------------------------------------------------------------------------
# sparks
# --------------------------------------------------------------------------

SPARKS = [
    "falconry", "beekeeping", "glassblowing", "lighthouse keeping", "competitive sailing", "mycology",
    "medieval cartography", "watchmaking", "volcanology", "perfumery", "bonsai", "sumo wrestling",
    "hot-air ballooning", "pigeon racing", "letterpress printing", "cheese making", "deep-sea diving",
    "origami", "jazz improvisation", "tea ceremony", "ballet", "surf forecasting", "fermentation",
    "heraldry", "rock climbing", "calligraphy", "natural dye making", "mountaineering", "stonemasonry",
    "bridge engineering", "orchid growing", "astronomy and star catalogues", "knot tying", "beat making",
    "circus aerial arts", "archery", "gemology", "shipbuilding", "violin making", "desert botany",
    "polar exploration", "bird migration", "coral reef ecology", "fencing", "chess openings",
    "railway history", "typography and type design", "perfume chemistry", "blacksmithing", "kite flying",
    "puppetry", "lacemaking", "cave exploration", "weather forecasting", "honey varieties", "ice climbing",
    "film editing", "stage lighting", "acoustics and concert halls", "rowing", "salt making",
    "coffee roasting", "mapmaking and surveying", "lock picking (locksmithing)", "clockwork automata",
    "bread baking", "wine tasting vocabulary", "rug weaving", "pottery glazes", "sailing knots",
    "aviation history", "paper making", "fly fishing", "competitive cycling", "marathon running",
    "trail tracking", "astronaut training", "ocean currents", "tide tables", "seed saving",
    "architecture of domes", "stained glass", "drum making", "choir singing", "radio broadcasting",
    "morse code", "semaphore and signal flags", "mineral collecting", "fossil hunting", "botanical illustration",
    "sword forging", "horse dressage", "sheepdog trials", "luthiery", "vintage motorcycles",
    "formula racing pit crews", "air traffic control", "submarine navigation", "glacier science",
    "lighthouse lenses", "candle making", "spice trading routes", "silk production", "the history of maps",
    "magic tricks and stagecraft", "juggling", "skateboarding", "snowflake science", "wind energy",
    "solar sailing", "geyser science", "rainforest canopies", "desert nomad navigation", "camel caravans",
    "migratory whales", "fireflies", "bioluminescence", "the periodic table's discoverers", "ancient libraries",
    "codebreaking", "carnival rides", "roller coaster engineering", "tightrope walking", "parkour",
    "free diving", "cloud classification", "rainbows and optics", "prisms and lenses", "kaleidoscopes",
    "jewellery making", "shoe making", "tailoring", "hat making", "barbering", "street food markets",
    "night markets", "bridge games and card play", "board game design", "puzzle making", "crossword setting",
    "orchestral conducting", "opera", "folk dance", "drumlines", "national parks rangers",
    "wildlife photography", "beach combing", "shell collecting", "sand dune ecology", "salt flats",
    "the Silk Road", "trade winds", "constellations of the southern sky", "rocket staging",
    "spacewalks", "satellite orbits", "the deep ocean's twilight zone", "octopus intelligence",
    "ant colonies", "bee dances", "swarm robotics", "origami in space engineering", "gliders and soaring",
]


def cmd_sparks(args):
    rng = random.Random(args.seed) if args.seed is not None else random.SystemRandom()
    pool = list(dict.fromkeys(SPARKS))
    n = max(1, min(args.n, len(pool)))
    picks = rng.sample(pool, n)
    for i, p in enumerate(picks, 1):
        print(f"{i}. {p}")
    return 0


# --------------------------------------------------------------------------
# handles
# --------------------------------------------------------------------------

def cmd_handles(args):
    tlds = args.tlds or [".com", ".co", ".io", ".app"]
    if args.cc:
        cc = args.cc.lower().lstrip(".")
        extra = {"za": [".co.za"], "uk": [".co.uk"], "au": [".com.au"], "nz": [".co.nz"],
                 "in": [".in", ".co.in"], "br": [".com.br"], "jp": [".jp", ".co.jp"]}.get(cc, [f".{cc}"])
        tlds = tlds + extra
    for name in args.names:
        s = slug(name)
        print(f"## {name}")
        print("domains:  " + ", ".join(f"{s}{t}" for t in tlds))
        print("variants: " + ", ".join(f"{p}{s}.com" for p in ("get", "try", "use", "hello", "join"))
              + ", " + ", ".join(f"{s}{x}.com" for x in ("hq", "app", "labs")))
        print(f"handles:  @{s}, @{s}hq, @get{s}, @{s}app")
        print()
    print("Check each live: what is on the domain now, who holds the handle, and what a search for the "
          "name returns in your category.")
    return 0


# --------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("check", help="validate team JSONL files")
    p.add_argument("files", nargs="+")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("merge", help="merge team JSONL files and print the sonar readout")
    p.add_argument("files", nargs="+", help="files or glob patterns (quote ** patterns)")
    p.add_argument("--out", help="write merged JSON here")
    p.add_argument("--top", type=int, default=20, help="territories to show (default 20)")
    p.set_defaults(func=cmd_merge)

    p = sub.add_parser("phonetics", help="structure and sound-symbolism readout")
    p.add_argument("names", nargs="*")
    p.add_argument("--from", dest="from_file", help="JSON file with a list of names or {name: ...} objects")
    p.add_argument("--profile", nargs="*", help="desired feel, e.g. fast light reliable warm")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_phonetics)

    p = sub.add_parser("sparks", help="draw random far domains for synchronicity")
    p.add_argument("--n", type=int, default=4)
    p.add_argument("--seed", type=int)
    p.set_defaults(func=cmd_sparks)

    p = sub.add_parser("handles", help="domain and handle variants to check")
    p.add_argument("names", nargs="+")
    p.add_argument("--tlds", nargs="*")
    p.add_argument("--cc", help="country code for a local TLD, e.g. za, uk, au")
    p.set_defaults(func=cmd_handles)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
