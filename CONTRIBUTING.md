# Contributing

Discuss substantial changes in an issue before opening a pull request. Small fixes
can go straight to a pull request. Follow the code of conduct.

Use Python 3.9+ and Node.js 22+ for development:

```bash
npm ci --ignore-scripts
./scripts/test-all.sh
python3 scripts/package.py
```

No model account or API key is needed for these checks. `scripts/smoke.py` is an
optional live-model evaluation; it requires a configured harness and can incur
usage costs. Never commit its raw outputs or personal prompts.

Keep skill names and descriptions valid under the Agent Skills specification.
Keep the two plugin manifests identical and marketplace versions consistent.
Update the changelog for user-facing changes. Preserve upstream license notices
and record source commits in `sources.json` when importing or updating content.

For Thai writing changes, include constructed before/after examples, intended
register, and evidence that meaning, negation, numbers and technical identifiers
are preserved. Avoid treating stylistic preferences as universal grammar rules.
Use synthetic test inputs; never add real IDs, addresses, private URLs or tokens.
Utility and installer changes need meaningful regression checks. Documentation
changes need link and manifest validation, not tests that repeat their wording.
