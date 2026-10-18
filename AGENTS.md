Skills are organized into bucket folders under `skills/`, one bucket per domain:

- `branding/`: naming and brand decisions
- `product/`: deciding what to build and making it engaging

Add a new bucket when a skill doesn't fit an existing one. Don't put unrelated skills in the same bucket.

Every skill lives at `skills/<bucket>/<skill-name>/` with a `SKILL.md` whose `name` matches the folder. Supporting files (`references/`, `assets/`, `scripts/`, subagent briefs) sit inside the skill folder. Each skill also has `agents/openai.yaml` with a `display_name` and `short_description` for Codex.

To add a skill, run `scripts/new-skill.sh <bucket> <skill-name> "<one-line description>"`. It scaffolds the files and does steps 1–3 below, plus the docs stub for step 4. Then run `scripts/check-skills.sh`, which fails if any of the wiring below is missing.

When you add, rename or remove a skill, update all of these together:

1. `.claude-plugin/plugin.json`: the `skills` array lists every shipped skill's folder.
2. The bucket's `README.md`: one line per skill, with the name linked to its `SKILL.md`, grouped into **User-invoked** and **Model-invoked**.
3. The top-level `README.md`: the same entry under its bucket heading, plus any credit.
4. `docs/<bucket>/<skill-name>.md`: the human-facing docs page, with **What it does**, **When to reach for it**, **It's working if**, **Common questions** and **Where it fits**.

A skill is model-invoked by default (model- or user-reachable). To make it user-invoked only, add `disable-model-invocation: true` to its frontmatter and `policy.allow_implicit_invocation: false` to `agents/openai.yaml`.

Run `claude plugin validate .` and `claude plugin validate .claude-plugin/plugin.json` after touching either manifest. Both should pass. The only expected warning is that the root `CLAUDE.md` isn't shipped as plugin context, which is intended: it's for contributors to this repo, not for people who install the plugin.

`scripts/list-skills.sh` lists every skill. `scripts/check-skills.sh` verifies the wiring. `scripts/link-skills.sh` symlinks them into `~/.claude/skills` and `~/.agents/skills` for local use. `scripts/package-skills.sh` builds uploadable `.skill` archives in `dist/` (gitignored).

Skills distilled from books, talks or other people's work must be written in our own words, credit the source in the docs page and README, and say they aren't affiliated with the author.
