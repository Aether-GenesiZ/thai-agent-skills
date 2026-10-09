# Verification on this machine — 2026-10-10 (Asia/Bangkok)

Installed one package containing 13 skills via copied skill directories. The final
install checks compare all file contents with source hashes, not just file existence.

| Harness | Installation/discovery | Model smoke test |
| --- | --- | --- |
| Claude Code 2.1.284 | 13 valid skills in `~/.claude/skills`; native component validator passes | Pass on configured GLM-5.3; initial added-action error corrected and retested |
| Codex CLI 0.162.1 | 13 valid skills in `~/.codex/skills` | Pass; JSONL records actual read of installed thai-language/SKILL.md |
| Hermes 0.21.5 | 13 skills in root profile; skills tool lists and views the core | Pass with explicit native `-s thai-language` preload |
| agy CLI | 13 skills in `~/.gemini/antigravity-cli/skills`; native validator processes 13 | Blocked by account HTTP 429 quota; default and GPT-OSS requests both rejected |
| Antigravity IDE | Same 13 skills in `~/.gemini/antigravity/skills`; hash verification passes | GUI session not exercised |

Hermes named-profile inherits `~/.hermes/skills` through its existing `external_dirs` config.
Profile-local duplicates were removed using the installer receipt after a runtime
collision was found. The configured model request failed with unavailable `GEMMA-4`;
a separate test uses a session-only GLM-5.3 override without changing its configuration.
That session-only test passes all smoke checks, including skill preload.

## Scope of the model smoke task

Each harness receives a short Thai prompt asking it to load the installed skill, name
one rule, compose a neutral team review request, translate may/must faithfully, and
translate the failed-save UI state. No skill body is injected into the test prompt.
Claude permits Read/Skill tools; Codex uses a read-only sandbox; Hermes uses only the
skills toolset and native preload. Small semantic checks flag missing deadlines,
negation, obligations, gendered particles and an unrequested return-delivery action.

These checks establish a small working integration; they are not a score for Thai
fluency and do not prove that a weak model improves across long-form genres. The final
Thai samples are stored in `evals/verification.json`. Raw traces/usage reports stay
locally in `evals/results/`; they are not part of the distributable archive.

## Other checks

- Upstream Boom-Vitt suite: 8 test groups pass.
- Upstream kien-thai default suite: 53 passed, 1 skipped, 21 deselected.
- Merged suite: 9 groups pass, including 7 installer/date regression tests.
- Strict YAML/frontmatter validation: all 13 skills pass the skill-creator validator.
- Claude native plugin/marketplace/component validation: passes.
- AGY root plugin validation: passes, with 13 skills processed.
- ZIP: CRC integrity and all 13 manifest skill paths checked.

Use a new session to discover the added skills. Existing gateways/conversations were
not restarted. AGY's account quota must recover before its end-to-end model test can
be rerun with `python3 scripts/smoke.py --harness agy`.
