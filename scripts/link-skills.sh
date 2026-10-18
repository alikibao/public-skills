#!/usr/bin/env bash
set -euo pipefail

# Symlinks every skill in this repo into the local skill directories:
#   - ~/.claude/skills: Claude Code
#   - ~/.agents/skills: Codex and other Agent Skills-compatible harnesses
# Because each entry is a symlink into this repo, `git pull` keeps the installed
# skills current. Re-run after adding, removing or renaming a skill.

REPO="$(cd "$(dirname "$0")/.." && pwd)"
DESTS=("$HOME/.claude/skills" "$HOME/.agents/skills")

srcs=()
while IFS= read -r -d '' skill_md; do
  srcs+=("$(dirname "$skill_md")")
done < <(find "$REPO/skills" -name SKILL.md -print0)

for DEST in "${DESTS[@]}"; do
  # Refuse to write links back into the repo if $DEST itself points here.
  if [ -L "$DEST" ]; then
    resolved="$(readlink -f "$DEST")"
    case "$resolved" in
      "$REPO"|"$REPO"/*)
        echo "error: $DEST is a symlink into this repo ($resolved). Remove it and re-run." >&2
        exit 1
        ;;
    esac
  fi

  mkdir -p "$DEST"

  for src in "${srcs[@]}"; do
    name="$(basename "$src")"
    target="$DEST/$name"
    if [ -e "$target" ] && [ ! -L "$target" ]; then
      echo "skip $name: $target exists and is not a symlink" >&2
      continue
    fi
    ln -sfn "$src" "$target"
    echo "linked $name -> $src ($DEST)"
  done
done
