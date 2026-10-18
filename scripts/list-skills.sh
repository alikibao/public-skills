#!/usr/bin/env bash
set -euo pipefail

# Lists every SKILL.md in the repo, relative to the repo root.

REPO="$(cd "$(dirname "$0")/.." && pwd)"

cd "$REPO"
find skills -name SKILL.md | sort
