#!/usr/bin/env bash
set -euo pipefail

# Scaffolds a new skill and registers it everywhere this repo expects.
#
#   ./scripts/new-skill.sh <bucket> <skill-name> "<one-line description>"
#
# Creates:
#   skills/<bucket>/<skill-name>/SKILL.md
#   skills/<bucket>/<skill-name>/agents/openai.yaml
#   skills/<bucket>/README.md        (if the bucket is new)
#   docs/<bucket>/<skill-name>.md
# Updates:
#   .claude-plugin/plugin.json        (adds the skill path)
#   skills/<bucket>/README.md         (adds a Model-invoked entry)
#   README.md                         (adds the bucket section and entry)
#
# Then fill in the TODOs and run ./scripts/check-skills.sh.

if [ $# -lt 3 ]; then
  echo "usage: $0 <bucket> <skill-name> \"<one-line description>\"" >&2
  exit 1
fi

BUCKET="$1"
NAME="$2"
DESC="$3"
REPO="$(cd "$(dirname "$0")/.." && pwd)"

for v in "$BUCKET" "$NAME"; do
  if ! [[ "$v" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
    echo "error: '$v' must be lowercase kebab-case (e.g. pricing-strategy)" >&2
    exit 1
  fi
done

SKILL_DIR="$REPO/skills/$BUCKET/$NAME"
if [ -e "$SKILL_DIR" ]; then
  echo "error: $SKILL_DIR already exists" >&2
  exit 1
fi
if find "$REPO/skills" -mindepth 2 -maxdepth 2 -type d -name "$NAME" | grep -q .; then
  echo "error: a skill named '$NAME' already exists in another bucket" >&2
  exit 1
fi

mkdir -p "$SKILL_DIR/agents" "$REPO/docs/$BUCKET"

cat > "$SKILL_DIR/SKILL.md" <<EOF
---
name: $NAME
description: TODO. What the skill does and when to use it, including the phrases and situations that should trigger it. Max 1024 characters.
---

# TODO: Title

TODO: instructions. Keep this file under ~500 lines and move detail into
references/ files that this file points to.
EOF

DISPLAY="$(echo "$NAME" | tr '-' ' ' | awk '{for(i=1;i<=NF;i++) $i=toupper(substr($i,1,1)) substr($i,2)} 1')"
cat > "$SKILL_DIR/agents/openai.yaml" <<EOF
interface:
  display_name: "$DISPLAY"
  short_description: "TODO: under 60 characters"
EOF

cat > "$REPO/docs/$BUCKET/$NAME.md" <<EOF
## What it does

TODO

## When to reach for it

TODO

## It's working if

- TODO

## Common questions

**TODO?**
TODO

## Where it fits

TODO
EOF

python3 - "$REPO" "$BUCKET" "$NAME" "$DESC" <<'PY'
import json, os, re, sys
repo, bucket, name, desc = sys.argv[1:]
title = bucket.replace('-', ' ').title()

# plugin.json
p = os.path.join(repo, '.claude-plugin', 'plugin.json')
d = json.load(open(p))
path = f'./skills/{bucket}/{name}'
if path not in d['skills']:
    d['skills'].append(path)
    d['skills'].sort()
json.dump(d, open(p, 'w'), indent=2)
open(p, 'a').write('\n')

# bucket README
br = os.path.join(repo, 'skills', bucket, 'README.md')
entry = f'- **[{name}](./{name}/SKILL.md)**: {desc}\n'
if not os.path.exists(br):
    open(br, 'w').write(
        f'# {title}\n\nTODO: one line on what this bucket is for.\n\n'
        '## Model-invoked\n\n'
        'Model- or user-reachable (rich trigger phrasing so the model can reach for them).\n\n'
        + entry)
else:
    s = open(br).read()
    if '## Model-invoked' in s:
        s = s.rstrip('\n') + '\n' + entry
    else:
        s = s.rstrip('\n') + '\n\n## Model-invoked\n\n' + entry
    open(br, 'w').write(s)

# top-level README: add under "### <Title>" inside "## Reference", creating the section if needed
r = os.path.join(repo, 'README.md')
s = open(r).read()
top_entry = (f'- **[{name}](./skills/{bucket}/{name}/SKILL.md)**: {desc} '
             f'[Docs](./docs/{bucket}/{name}.md).\n')
heading = f'### {title}\n'
if heading in s:
    start = s.index(heading)
    nxt = re.search(r'\n(### |## )', s[start + len(heading):])
    end = start + len(heading) + (nxt.start() + 1 if nxt else len(s) - start - len(heading))
    section = s[start:end].rstrip('\n') + '\n' + top_entry + '\n'
    s = s[:start] + section + s[end:]
else:
    block = (f'{heading}\nTODO: one line on this bucket. '
             f'[Bucket README](./skills/{bucket}/README.md)\n\n{top_entry}\n')
    for marker in ('## Adding a skill', '## Credits'):
        if marker in s:
            s = s.replace(marker, block + marker, 1)
            break
    else:
        s = s.rstrip('\n') + '\n\n' + block
open(r, 'w').write(s)
PY

echo "created skills/$BUCKET/$NAME"
echo "next:"
echo "  1. write skills/$BUCKET/$NAME/SKILL.md (frontmatter description is what triggers it)"
echo "  2. fill in agents/openai.yaml, docs/$BUCKET/$NAME.md and any TODOs in the READMEs"
echo "  3. add a credit to README.md if the skill is based on someone else's work"
echo "  4. run ./scripts/check-skills.sh"
