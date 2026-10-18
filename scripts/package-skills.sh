#!/usr/bin/env bash
set -euo pipefail

# Builds an uploadable <skill-name>.skill archive (a zip) for every skill, in
# dist/ (gitignored). Use these to upload a skill in the Claude apps
# (Settings > Capabilities > Skills) or to attach to a GitHub release.

REPO="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$REPO/dist"
mkdir -p "$OUT"

while IFS= read -r -d '' skill_md; do
  src="$(dirname "$skill_md")"
  name="$(basename "$src")"
  rm -f "$OUT/$name.skill"
  (cd "$(dirname "$src")" && zip -qr "$OUT/$name.skill" "$name" -x '*/__pycache__/*' '*.pyc' '*/.DS_Store')
  echo "packaged $name -> dist/$name.skill"
done < <(find "$REPO/skills" -name SKILL.md -print0)
