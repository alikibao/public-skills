#!/usr/bin/env bash
set -euo pipefail

# Checks that every skill is wired up the way AGENTS.md describes:
# valid frontmatter, name matches folder, agents/openai.yaml, docs page,
# bucket README entry, top-level README entry, and a plugin.json entry
# (and that plugin.json lists nothing that doesn't exist).

REPO="$(cd "$(dirname "$0")/.." && pwd)"

python3 - "$REPO" <<'PY'
import json, os, re, sys
repo = sys.argv[1]
errors, todos = [], []

skills = []
for root, dirs, files in os.walk(os.path.join(repo, 'skills')):
    if 'SKILL.md' in files:
        rel = os.path.relpath(root, repo)
        parts = rel.split(os.sep)
        if len(parts) != 3:
            errors.append(f'{rel}: skills must live at skills/<bucket>/<skill-name>/')
            continue
        skills.append((parts[1], parts[2], root))
        dirs[:] = []

plugin = json.load(open(os.path.join(repo, '.claude-plugin', 'plugin.json')))
listed = set(plugin.get('skills', []))
top = open(os.path.join(repo, 'README.md')).read()

for bucket, name, root in sorted(skills):
    tag = f'{bucket}/{name}'
    s = open(os.path.join(root, 'SKILL.md')).read()
    m = re.match(r'^---\n(.*?)\n---\n', s, re.S)
    if not m:
        errors.append(f'{tag}: SKILL.md has no frontmatter')
    else:
        fm = m.group(1)
        nm = re.search(r'^name:\s*(.+)$', fm, re.M)
        ds = re.search(r'^description:\s*(.+)$', fm, re.M)
        if not nm or nm.group(1).strip() != name:
            errors.append(f'{tag}: frontmatter name must be "{name}"')
        if not ds:
            errors.append(f'{tag}: frontmatter description missing')
        elif len(ds.group(1).strip()) > 1024:
            errors.append(f'{tag}: description is {len(ds.group(1).strip())} chars (max 1024)')
    if not os.path.exists(os.path.join(root, 'agents', 'openai.yaml')):
        errors.append(f'{tag}: missing agents/openai.yaml')
    if not os.path.exists(os.path.join(repo, 'docs', bucket, f'{name}.md')):
        errors.append(f'{tag}: missing docs/{bucket}/{name}.md')
    br = os.path.join(repo, 'skills', bucket, 'README.md')
    if not os.path.exists(br) or f'(./{name}/SKILL.md)' not in open(br).read():
        errors.append(f'{tag}: not listed in skills/{bucket}/README.md')
    if f'(./skills/{bucket}/{name}/SKILL.md)' not in top:
        errors.append(f'{tag}: not listed in README.md')
    if f'./skills/{bucket}/{name}' not in listed:
        errors.append(f'{tag}: not in .claude-plugin/plugin.json skills')
    for f in [os.path.join(root, 'SKILL.md'), os.path.join(root, 'agents', 'openai.yaml'),
              os.path.join(repo, 'docs', bucket, f'{name}.md')]:
        if os.path.exists(f) and 'TODO' in open(f).read():
            todos.append(os.path.relpath(f, repo))

existing = {f'./skills/{b}/{n}' for b, n, _ in skills}
for p in sorted(listed - existing):
    errors.append(f'plugin.json lists {p}, which has no SKILL.md')

for t in todos:
    print(f'todo: {t} still has TODOs')
for e in errors:
    print(f'error: {e}')
print(f'{len(skills)} skills checked, {len(errors)} errors')
sys.exit(1 if errors else 0)
PY
