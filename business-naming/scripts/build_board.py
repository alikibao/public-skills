#!/usr/bin/env python3
"""Build the proof-of-concept board: every finalist shown in real-world contexts.

Clients judge names badly in a list and well in context. This script turns the
final names into one self-contained HTML page where each name appears as a
news headline, a premium print ad, a product on a shelf, an app on a phone, a
sign, and a line in conversation.

Usage
  python build_board.py final.json --out board.html

Input JSON
{
  "project": "Working title of the project",
  "category": "fiber supplement",            # what it is, in plain words
  "intro": "One short paragraph framing the shortlist (optional)",
  "names": [
    {
      "name": "Feather",                      # required
      "descriptor": "The lightweight fiber you need",
      "type": "real word, new context",
      "territory": "Lightness",
      "zone": "tension",                      # tension | invisible | noise
      "gut": 9,                               # 1-10, no sevens
      "recommended": true,
      "says": "One line on what the name says",
      "story": "2-3 sentences on why this name",
      "headline": "A believable news headline",
      "ad_line": "A line for a premium print ad",
      "in_use": "A sentence of the name used in real life",
      "believable": "yes",                    # yes | stretch | no
      "domain": "feather.co",                 # optional
      "risks": ["Preliminary screen: ..."]
    }
  ],
  "off_table": [ {"name": "...", "note": "why it still has value"} ]
}
Only "project" and names[].name are required; missing fields are skipped.
"""

import argparse
import hashlib
import html
import json
import re
import sys
from pathlib import Path


def esc(value) -> str:
    return html.escape(str(value), quote=True) if value is not None else ""


def slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]", "", name.lower()) or "name"


def hue_for(name: str) -> int:
    return int(hashlib.sha1(name.encode("utf-8")).hexdigest()[:6], 16) % 360


ZONE_LABEL = {
    "tension": "Tension zone",
    "invisible": "Invisible zone",
    "noise": "Noise zone",
}

CSS = r"""
:root{
  --bg:#f6f4ef; --surface:#ffffff; --surface-2:#efece5; --ink:#1b1a17; --muted:#6b675e;
  --line:#dcd7cc; --accent:#b4471f; --accent-ink:#ffffff;
  --tension:#b4471f; --invisible:#7a776f; --noise:#6a4bb3;
  --paper:#fbfaf6; --paper-ink:#1b1a17; --ad-bg:#161513; --ad-ink:#f3f1ea;
  --phone:#1e1e22; --phone-ink:#f4f4f6;
  --radius:14px; --serif:"Fraunces", Georgia, "Times New Roman", serif;
  --sans:"Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --mono:"JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  color-scheme: light;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --bg:#121210; --surface:#1b1a18; --surface-2:#24231f; --ink:#f0ede6; --muted:#a39e93;
    --line:#34322d; --accent:#e0794f; --accent-ink:#1b1a17;
    --tension:#e0794f; --invisible:#9a968d; --noise:#a68cf0;
    --paper:#1f1e1b; --paper-ink:#f0ede6; color-scheme: dark;
  }
}
:root[data-theme="dark"]{
  --bg:#121210; --surface:#1b1a18; --surface-2:#24231f; --ink:#f0ede6; --muted:#a39e93;
  --line:#34322d; --accent:#e0794f; --accent-ink:#1b1a17;
  --tension:#e0794f; --invisible:#9a968d; --noise:#a68cf0;
  --paper:#1f1e1b; --paper-ink:#f0ede6; color-scheme: dark;
}
*{box-sizing:border-box}
html,body{margin:0}
body{background:var(--bg); color:var(--ink); font-family:var(--sans); line-height:1.5;
  -webkit-font-smoothing:antialiased; overflow-x:hidden}
.wrap{max-width:1180px; margin:0 auto; padding:32px 16px 64px}
header.top{display:flex; flex-wrap:wrap; gap:16px 32px; align-items:flex-end; justify-content:space-between;
  border-bottom:1px solid var(--line); padding-bottom:24px; margin-bottom:24px}
.eyebrow{font:600 12px/1 var(--sans); letter-spacing:.14em; text-transform:uppercase; color:var(--muted)}
h1{font-family:var(--serif); font-weight:600; font-size:clamp(30px,5vw,48px); line-height:1.05; margin:8px 0 6px}
.intro{max-width:62ch; color:var(--muted); margin:0}
.controls{display:flex; gap:8px; flex-wrap:wrap; align-items:center}
.seg{display:inline-flex; border:1px solid var(--line); border-radius:999px; overflow:hidden; background:var(--surface)}
.seg button{all:unset; cursor:pointer; padding:7px 14px; font:500 13px/1 var(--sans); color:var(--muted)}
.seg button[aria-pressed="true"]{background:var(--ink); color:var(--bg)}
.seg button:focus-visible{outline:2px solid var(--accent); outline-offset:-2px}
nav.chips{display:flex; flex-wrap:wrap; gap:8px; margin:0 0 32px}
nav.chips a{text-decoration:none; color:var(--ink); background:var(--surface); border:1px solid var(--line);
  border-radius:999px; padding:6px 12px; font-size:14px}
nav.chips a.rec{border-color:var(--accent)}
nav.chips a.rec::before{content:"\2605 "; color:var(--accent)}
.legend{display:flex; gap:16px; flex-wrap:wrap; font-size:13px; color:var(--muted); margin:-16px 0 28px}
.dot{display:inline-block; width:9px; height:9px; border-radius:50%; margin-right:6px; vertical-align:middle}
section.name{background:var(--surface); border:1px solid var(--line); border-radius:var(--radius);
  padding:28px 24px; margin:0 0 28px; scroll-margin-top:16px}
.hero{display:flex; flex-wrap:wrap; justify-content:space-between; gap:12px 24px; align-items:flex-end;
  padding-bottom:20px; border-bottom:1px solid var(--line); margin-bottom:22px}
.wordmark{font-size:clamp(44px,9vw,92px); line-height:.95; letter-spacing:-.02em; margin:0; word-break:break-word}
body[data-face="serif"] .wordmark{font-family:var(--serif); font-weight:600}
body[data-face="sans"] .wordmark{font-family:var(--sans); font-weight:800; letter-spacing:-.04em}
body[data-face="mono"] .wordmark{font-family:var(--mono); font-weight:600; letter-spacing:-.03em}
body[data-face="lower"] .wordmark{font-family:var(--sans); font-weight:700; text-transform:lowercase; letter-spacing:-.04em}
.descriptor{font-size:18px; color:var(--muted); margin:10px 0 0}
.meta{display:flex; flex-wrap:wrap; gap:8px; justify-content:flex-end}
.pill{font-size:12px; border:1px solid var(--line); border-radius:999px; padding:4px 10px; color:var(--muted); white-space:nowrap}
.pill.zone{color:var(--accent-ink); border:0}
.pill.rec{background:var(--accent); color:var(--accent-ink); border:0; font-weight:600}
.grid{display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:16px}
.tile{border:1px solid var(--line); border-radius:12px; overflow:hidden; min-height:220px; display:flex; flex-direction:column}
.tile .cap{font:600 11px/1 var(--sans); letter-spacing:.12em; text-transform:uppercase; color:var(--muted);
  padding:10px 12px; border-top:1px solid var(--line); background:var(--surface-2); margin-top:auto}
/* newspaper */
.paper{background:var(--paper); color:var(--paper-ink); padding:16px; flex:1}
.paper .mast{font-family:var(--serif); font-weight:700; text-align:center; font-size:15px; letter-spacing:.06em;
  border-bottom:2px solid currentColor; padding-bottom:6px; margin-bottom:10px}
.paper .hl{font-family:var(--serif); font-weight:600; font-size:20px; line-height:1.18; margin:0 0 8px}
.paper .lede{font-size:12.5px; line-height:1.45; opacity:.8; columns:2; column-gap:14px; margin:0}
/* ad */
.ad{background:var(--ad-bg); color:var(--ad-ink); flex:1; display:flex; flex-direction:column; justify-content:flex-end;
  padding:18px; position:relative; overflow:hidden; min-height:230px}
.ad::before{content:""; position:absolute; inset:0;
  background:radial-gradient(120% 80% at 75% 10%, rgba(255,255,255,.22), transparent 55%),
             radial-gradient(70% 60% at 15% 25%, rgba(255,255,255,.10), transparent 60%),
             linear-gradient(160deg, #2a2926 0%, #0f0f0e 100%)}
.ad > *{position:relative}
.ad .line{font-family:var(--serif); font-style:italic; font-size:19px; line-height:1.25; margin:0 0 14px}
.ad .sig{font-weight:700; letter-spacing:.02em}
/* shelf */
.shelf{flex:1; display:flex; align-items:flex-end; justify-content:center; gap:10px; padding:16px 12px 0;
  background:linear-gradient(var(--surface-2), var(--surface-2)) bottom/100% 14px no-repeat, var(--surface)}
.pack{width:44%; aspect-ratio:3/4.2; border-radius:10px 10px 4px 4px; color:#fff; padding:14px 12px; display:flex;
  flex-direction:column; justify-content:space-between; box-shadow:0 10px 24px rgba(0,0,0,.18); margin-bottom:14px}
.pack.ghost{width:22%; aspect-ratio:3/4.6; background:var(--line); box-shadow:none; opacity:.7}
.pack .pn{font-weight:800; font-size:clamp(16px,2.2vw,22px); line-height:1; letter-spacing:-.02em; word-break:break-word}
.pack .pd{font-size:10.5px; line-height:1.3; opacity:.92}
.pack .pc{font:600 9px/1 var(--sans); letter-spacing:.14em; text-transform:uppercase; opacity:.85}
/* phone */
.phonewrap{flex:1; display:flex; justify-content:center; align-items:center; padding:14px; background:var(--surface-2)}
.phone{width:min(100%,210px); background:var(--phone); color:var(--phone-ink); border-radius:26px; padding:14px 12px 16px}
.notif{background:rgba(255,255,255,.12); border-radius:12px; padding:8px 10px; font-size:11px; line-height:1.35; margin-bottom:12px}
.notif b{display:block; font-size:11.5px}
.apps{display:grid; grid-template-columns:repeat(4,1fr); gap:10px 8px}
.app{display:flex; flex-direction:column; align-items:center; gap:4px; font-size:9.5px; text-align:center; opacity:.55}
.app i{display:block; width:34px; height:34px; border-radius:9px; background:rgba(255,255,255,.18)}
.app.me{opacity:1}
.app.me i{display:grid; place-items:center; font-style:normal; font-weight:800; font-size:17px; color:#fff}
/* sign */
.sign{flex:1; display:flex; align-items:center; justify-content:center; padding:22px 16px;
  background:linear-gradient(180deg,#2b2d31 0%, #3a3d42 60%, #55585e 100%)}
.board{background:#0e0f10; border:6px solid #1c1d1f; border-radius:6px; padding:18px 22px; text-align:center;
  box-shadow:0 0 0 2px #444 inset, 0 14px 30px rgba(0,0,0,.35); max-width:100%}
.board .bn{font-weight:800; font-size:clamp(24px,3.4vw,36px); line-height:1; letter-spacing:-.01em; word-break:break-word}
.board .bd{font-size:12px; color:#c9c9c9; margin-top:6px}
/* talk */
.talk{flex:1; padding:14px; display:flex; flex-direction:column; gap:10px; background:var(--surface)}
.url{font:12px/1 var(--mono); background:var(--surface-2); border:1px solid var(--line); border-radius:999px;
  padding:8px 12px; color:var(--muted); white-space:nowrap; overflow:hidden; text-overflow:ellipsis}
.url b{color:var(--ink); font-weight:600}
.bubble{align-self:flex-start; max-width:92%; background:var(--surface-2); border-radius:16px 16px 16px 4px;
  padding:9px 12px; font-size:14px}
.bubble.me{align-self:flex-end; background:var(--accent); color:var(--accent-ink); border-radius:16px 16px 4px 16px}
.why{display:grid; grid-template-columns:2fr 1fr; gap:24px; margin-top:22px}
.why h3{font:600 12px/1 var(--sans); letter-spacing:.12em; text-transform:uppercase; color:var(--muted); margin:0 0 8px}
.why p{margin:0 0 10px; max-width:68ch}
.why ul{margin:0; padding-left:18px; color:var(--muted); font-size:14px}
.offtable{background:transparent; border:1px dashed var(--line)}
.offtable ul{columns:2; column-gap:32px; padding-left:18px}
.offtable li{break-inside:avoid; margin-bottom:8px}
footer{color:var(--muted); font-size:13px; border-top:1px solid var(--line); padding-top:18px; margin-top:12px}
@media (max-width:900px){ .grid{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media (max-width:620px){
  .wrap{padding:20px 16px 48px}
  section.name{padding:20px 16px}
  .grid{grid-template-columns:1fr}
  .why{grid-template-columns:1fr}
  .offtable ul{columns:1}
  .paper .lede{columns:1}
  .meta{justify-content:flex-start}
}
"""

JS = r"""
(function(){
  var body = document.body;
  function setFace(face){
    body.setAttribute('data-face', face);
    document.querySelectorAll('[data-face-btn]').forEach(function(b){
      b.setAttribute('aria-pressed', b.getAttribute('data-face-btn') === face ? 'true' : 'false');
    });
    try { localStorage.setItem('board-face', face); } catch(e) {}
  }
  document.querySelectorAll('[data-face-btn]').forEach(function(b){
    b.addEventListener('click', function(){ setFace(b.getAttribute('data-face-btn')); });
  });
  var saved = null;
  try { saved = localStorage.getItem('board-face'); } catch(e) {}
  if (saved) setFace(saved);
})();
"""


def first_sentence(text: str) -> str:
    if not text:
        return ""
    m = re.match(r"(.+?[.!?])(\s|$)", text.strip())
    return m.group(1) if m else text.strip()


def render_name(n: dict, category: str, idx: int) -> str:
    name = str(n.get("name", "")).strip()
    sid = slug(name) + f"-{idx}"
    hue = hue_for(name)
    pack_bg = f"linear-gradient(160deg, hsl({hue} 52% 36%), hsl({(hue + 28) % 360} 58% 24%))"
    icon_bg = f"hsl({hue} 55% 42%)"
    descriptor = n.get("descriptor") or ""
    zone = str(n.get("zone") or "").lower()
    gut = n.get("gut")
    domain = n.get("domain") or f"{slug(name)}.com"
    headline = n.get("headline") or f"{name} sets out to change how people think about {category}"
    ad_line = n.get("ad_line") or (descriptor or f"Introducing {name}.")
    story = n.get("story") or n.get("says") or ""
    in_use = n.get("in_use") or f"Have you tried {name} yet?"
    lede = story or descriptor

    meta = []
    if n.get("recommended"):
        meta.append('<span class="pill rec">Recommended</span>')
    if zone in ZONE_LABEL:
        meta.append(f'<span class="pill zone" style="background:var(--{zone})">{ZONE_LABEL[zone]}</span>')
    for key in ("type", "territory"):
        if n.get(key):
            meta.append(f'<span class="pill">{esc(n[key])}</span>')
    if gut not in (None, ""):
        meta.append(f'<span class="pill">Gut {esc(gut)}/10</span>')
    if n.get("believable") and str(n["believable"]).lower() != "yes":
        meta.append(f'<span class="pill">Believable: {esc(n["believable"])}</span>')

    risks = n.get("risks") or []
    if isinstance(risks, str):
        risks = [risks]
    risk_html = "".join(f"<li>{esc(r)}</li>" for r in risks) or "<li>No screening notes recorded.</li>"

    says = n.get("says")
    story_html = ""
    if says:
        story_html += f"<p><strong>{esc(says)}</strong></p>"
    if n.get("story") and n.get("story") != says:
        story_html += f"<p>{esc(n['story'])}</p>"

    initial = esc(name[:1].upper())
    return f"""
<section class="name" id="{sid}">
  <div class="hero">
    <div>
      <p class="wordmark">{esc(name)}</p>
      {f'<p class="descriptor">{esc(descriptor)}</p>' if descriptor else ''}
    </div>
    <div class="meta">{''.join(meta)}</div>
  </div>
  <div class="grid">
    <div class="tile">
      <div class="paper">
        <div class="mast">THE MORNING LEDGER</div>
        <p class="hl">{esc(headline)}</p>
        <p class="lede">{esc(lede)}</p>
      </div>
      <div class="cap">In the news</div>
    </div>
    <div class="tile">
      <div class="ad">
        <p class="line">{esc(ad_line)}</p>
        <div class="sig">{esc(name)}</div>
      </div>
      <div class="cap">Premium print ad</div>
    </div>
    <div class="tile">
      <div class="shelf">
        <div class="pack ghost"></div>
        <div class="pack" style="background:{pack_bg}">
          <div class="pc">{esc(category)}</div>
          <div class="pn">{esc(name)}</div>
          <div class="pd">{esc(descriptor)}</div>
        </div>
        <div class="pack ghost"></div>
      </div>
      <div class="cap">On the shelf</div>
    </div>
    <div class="tile">
      <div class="phonewrap">
        <div class="phone">
          <div class="notif"><b>{esc(name)}</b>{esc(first_sentence(descriptor) or 'Your order is on its way.')}</div>
          <div class="apps">
            <div class="app"><i></i>Mail</div><div class="app"><i></i>Maps</div>
            <div class="app me"><i style="background:{icon_bg}">{initial}</i>{esc(name[:12])}</div>
            <div class="app"><i></i>Notes</div><div class="app"><i></i>Photos</div>
            <div class="app"><i></i>Bank</div><div class="app"><i></i>Music</div><div class="app"><i></i>Clock</div>
          </div>
        </div>
      </div>
      <div class="cap">On a phone</div>
    </div>
    <div class="tile">
      <div class="sign">
        <div class="board">
          <div class="bn" style="color:hsl({hue} 80% 72%)">{esc(name)}</div>
          {f'<div class="bd">{esc(descriptor)}</div>' if descriptor else ''}
        </div>
      </div>
      <div class="cap">Sign &amp; storefront</div>
    </div>
    <div class="tile">
      <div class="talk">
        <div class="url">https://<b>{esc(domain)}</b></div>
        <div class="bubble">What are you using for that now?</div>
        <div class="bubble me">{esc(in_use)}</div>
        <div class="url">hello@<b>{esc(domain)}</b></div>
      </div>
      <div class="cap">Said out loud, typed in</div>
    </div>
  </div>
  <div class="why">
    <div>
      <h3>Why this name</h3>
      {story_html or '<p>—</p>'}
    </div>
    <div>
      <h3>Screening notes</h3>
      <ul>{risk_html}</ul>
    </div>
  </div>
</section>"""


def build(data: dict) -> str:
    project = str(data.get("project") or "Naming shortlist")
    category = str(data.get("category") or "")
    names = [n for n in data.get("names", []) if isinstance(n, dict) and str(n.get("name", "")).strip()]
    if not names:
        raise SystemExit("final.json has no names")

    chips = []
    for i, n in enumerate(names):
        cls = ' class="rec"' if n.get("recommended") else ""
        chips.append(f'<a href="#{slug(n["name"])}-{i}"{cls}>{esc(n["name"])}</a>')

    zones_used = sorted({str(n.get("zone", "")).lower() for n in names} & set(ZONE_LABEL))
    legend = ""
    if zones_used:
        explain = {
            "tension": "familiar enough to grasp, surprising enough to split the room — where strong names live",
            "invisible": "easy and safe, but blends into the category",
            "noise": "distinctive but hard to grasp",
        }
        legend = '<div class="legend">' + "".join(
            f'<span><span class="dot" style="background:var(--{z})"></span><b>{ZONE_LABEL[z]}</b> — {explain[z]}</span>'
            for z in zones_used) + "</div>"

    off = data.get("off_table") or []
    off_html = ""
    if off:
        items = []
        for o in off:
            if isinstance(o, str):
                items.append(f"<li><b>{esc(o)}</b></li>")
            elif isinstance(o, dict) and o.get("name"):
                note = o.get("note") or o.get("why") or ""
                items.append(f"<li><b>{esc(o['name'])}</b>{' — ' + esc(note) if note else ''}</li>")
        off_html = f"""
<section class="name offtable">
  <h3 class="eyebrow" style="margin:0 0 12px">Off the table — for now</h3>
  <p class="intro" style="margin-bottom:12px">Names with real energy that didn't make this round. Worth a second look once the shortlist has settled in.</p>
  <ul>{''.join(items)}</ul>
</section>"""

    intro = data.get("intro") or ("Read each name the way people will meet it — in a headline, on a shelf, "
                                  "on a phone, out loud — not in a list. Ask one question first: in the first "
                                  "second, do you lean toward believing it?")
    sections = "".join(render_name(n, category or "new", i) for i, n in enumerate(names))
    title = "Name Shortlist Board"

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,500;0,9..144,600;0,9..144,700;1,9..144,500&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body data-face="serif">
<div class="wrap">
  <header class="top">
    <div>
      <div class="eyebrow">Proof of concept{(' · ' + esc(category)) if category else ''}</div>
      <h1>{esc(project)}</h1>
      <p class="intro">{esc(intro)}</p>
    </div>
    <div class="controls" aria-label="Wordmark typeface">
      <div class="seg" role="group">
        <button type="button" data-face-btn="serif" aria-pressed="true">Serif</button>
        <button type="button" data-face-btn="sans" aria-pressed="false">Sans</button>
        <button type="button" data-face-btn="lower" aria-pressed="false">lowercase</button>
        <button type="button" data-face-btn="mono" aria-pressed="false">Mono</button>
      </div>
    </div>
  </header>
  <nav class="chips">{''.join(chips)}</nav>
  {legend}
  {sections}
  {off_html}
  <footer>Trademark, domain and language notes are preliminary screens, not legal clearance. Confirm finalists with an IP attorney and native speakers in each market before committing.</footer>
</div>
<script>{JS}</script>
</body>
</html>"""


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("final_json")
    ap.add_argument("--out", default="board.html")
    args = ap.parse_args(argv)
    with open(args.final_json, encoding="utf-8") as fh:
        data = json.load(fh)
    page = build(data)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(page, encoding="utf-8")
    print(f"Wrote {args.out} ({len(data.get('names', []))} names)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
