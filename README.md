# Public Skills

Agent skills for naming businesses, building products people love and putting AI to work in a business. They work in Claude Code, the Claude apps, Codex and other agents that support Agent Skills.

## Installation

<details>
<summary><strong>Claude Code</strong> (plugin, updates itself)</summary>

```bash
claude plugin marketplace add alikibao/public-skills
```

```bash
claude plugin install alikibao-skills@alikibao
```

</details>

<details>
<summary><strong>Claude apps</strong> (claude.ai and desktop)</summary>

Build the uploadable archives, then upload the ones you want in **Settings > Capabilities > Skills**:

```bash
./scripts/package-skills.sh
```

The archives land in `dist/` as `<skill-name>.skill`.

</details>

<details>
<summary><strong>Codex</strong></summary>

```bash
codex plugin marketplace add alikibao/public-skills
```

```bash
codex plugin add alikibao-skills@alikibao
```

</details>

<details>
<summary><strong>Any other agent, or editable files</strong></summary>

```bash
npx skills@latest add alikibao/public-skills
```

Or clone this repo and run `./scripts/link-skills.sh` to symlink every skill into `~/.claude/skills` and `~/.agents/skills`. After that, `git pull` keeps them up to date.

</details>

## Reference

Skills are grouped into buckets by domain. Every skill below is **model-invoked**: you can call it by name, and the agent also reaches for it on its own when your request fits.

### Branding

Naming and brand decisions. [Bucket README](./skills/branding/README.md)

- **[business-naming](./skills/branding/business-naming/SKILL.md)**: Name a business, product, app or brand the way a naming agency does: research, a creative framework, three independent naming teams, a separate judging room, language and trademark screening, and a proof-of-concept board of finalists. [Docs](./docs/branding/business-naming.md). Try: "Help me name my business."

### Product

Deciding what to build and making it engaging. [Bucket README](./skills/product/README.md)

- **[hit-products](./skills/product/hit-products/SKILL.md)**: Shape, test and grow products people keep coming back to. It separates the instinct from the idea, breaks ideas into Proven / Better / New, replaces the MVP with cheap tests and kill rules, grades ideas honestly, and designs engagement, retention and distribution. [Docs](./docs/product/hit-products.md). Try: "Is my app idea worth building?" or "How do we make our app stickier?"

### Business

Putting AI to work inside a business. [Bucket README](./skills/business/README.md)

- **[mission](./skills/business/mission/SKILL.md)**: Give your AI a mission. A grilling interview that starts from whatever problem you want AI to help with, works out what's really going on, and uncovers what your AI needs to know and do: the outcome, how the work really runs, the unwritten rules and judgement calls, and the limits. It ends with a brief to give your AI, or a plain "fix this first" when AI isn't the answer. [Docs](./docs/business/mission.md). Try: "I want AI to follow up our quotes" or "Our team won't use ChatGPT." No install needed: you can also paste the [SKILL.md](./skills/business/mission/SKILL.md) straight into ChatGPT or Claude.

## Adding a skill

```bash
./scripts/new-skill.sh <bucket> <skill-name> "<one-line description>"
```

This creates `skills/<bucket>/<skill-name>/` with a starter `SKILL.md` and `agents/openai.yaml`, plus a docs page at `docs/<bucket>/<skill-name>.md`. It also registers the skill in `.claude-plugin/plugin.json`, the bucket README and this README. A new bucket name creates the bucket. Fill in the TODOs, then run:

```bash
./scripts/check-skills.sh
```

The full conventions are in [AGENTS.md](./AGENTS.md).

## Licence

Use, change and share these skills however you like, including in paid work. No credit needed. They're released under [MIT No Attribution](./LICENSE).

## Credits

- **business-naming** is inspired by [David Placek's appearance in this video](https://www.youtube.com/watch?v=fDIW4W24VNk&t=1978s).
- **mission** adapts the grilling method from [Matt Pocock's skills](https://github.com/mattpocock/skills) (MIT licence), in its own words, for business owners rather than engineers. It isn't affiliated with or endorsed by Matt Pocock.
- **hit-products** is distilled from Mark Pincus's book *Life at the Speed of Play* and [his interview on Lenny's Podcast](https://www.youtube.com/watch?v=7eh9C3TUotc). It summarizes the ideas in its own words and isn't affiliated with or endorsed by the author.
