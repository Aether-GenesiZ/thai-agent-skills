# Public release review — 2026-10-12

Scope: current tracked files, all reachable Git history, skill and plugin manifests,
local Markdown links, license notices, package contents, installer regressions and
repository community files. This is a technical publication review, not a legal
opinion or a comprehensive Thai-language benchmark.

## Private assets and secrets

- No required private repository, private service endpoint, external corpus,
  model-routing hook, submodule or LFS asset was found.
- Gitleaks 8.30.1 scanned the full reachable commit history without findings.
  The official scanner download was verified against its published SHA-256.
- Removed a local named-profile identifier from file history and replaced
  machine-generated commit identity with a GitHub noreply identity. Original
  private history was retained locally outside the distribution.
- Raw live-model outputs, local configuration, credentials and generated builds
  are ignored. Packaging includes only explicitly allowed tracked files and
  rejects symlinks and sensitive file types. A regression verifies that untracked
  secrets cannot enter an archive.

## Attribution

Both source repositories are public, MIT licensed, and pinned in sources.json.
Their full license text and copyright notices are preserved. Corrected the old
notice that incorrectly described copied content as references only.

Province-data provenance remains less precise: the upstream reports Wikipedia
CC BY-SA input but omits article revisions. DATA_SOURCES.md records this limitation
and retains relevant attribution and share-alike conditions. The dataset is an
explicit exception to the blanket MIT statement. No private dataset is involved.

## Skill and public-repository checks

- Thirteen valid name/description frontmatters, checked with the local validator
  and an actual YAML parser; matching skill directories and manifests.
- Native Claude strict validation passed for both plugin and marketplace.
  Native agy validation processed all thirteen skills.
- No broken local Markdown links found. Optional upstream observations clearly
  identify their source and do not require downloading an external corpus.
- Added contribution, security, support, conduct and changelog documents, issue
  and pull-request templates, and dependency update configuration.
- CI uses read-only permissions and pinned GitHub Actions. It runs self-tests,
  package building, full-history secret scanning and Linux/Windows Python 3.9/
  3.13 installer regressions. Live-model tests are excluded.

The offline suite passes all nine groups, including eight regression tests.
See VERIFICATION.md for earlier live-model results and their provider limitations.
Future commits, new dependencies and releases require their own review.
