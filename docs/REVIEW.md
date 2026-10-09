# Review and merge notes

Sources and commits are pinned in `../sources.json`. Upstream clones remain unchanged;
forks are `SerusBusiness/claude-thai-skills` and `SerusBusiness/kien-thai`.
This is a content integration into one distributable package, not an unrelated-history
merge of both Git commit graphs.

## Confirmed defects and corrections

1. All twelve Boom-Vitt skills contain unquoted descriptions with colon-space text.
   A real YAML parser rejects them, although the upstream flat-string validator reports
   success. The merged files use JSON-quoted scalars (valid YAML), and our validator
   rejects unsafe unquoted descriptions, duplicate keys, and naming/length violations.
2. Date parsers discard explicit era markers and instead guess from the numeric year.
   `16 พ.ค. ค.ศ. 2569` incorrectly becomes CE 2026, while BE 2300 becomes CE 2300.
   Both Python and TypeScript now honor explicit markers, require four digits with an
   explicit era, and reject trailing junk. Unmarked short years retain the documented
   upstream heuristic; material date ambiguities should be clarified by the agent.
3. JavaScript Date silently rolls invalid dates such as 31 February into March.
   The TypeScript parser now checks calendar fields and rejects invalid input, matching
   Python behavior. Dates are local civil dates; do not serialize local midnight with
   `toISOString()` and expect its UTC date to match in every timezone.
4. Original translation guidance raises formality automatically and suggests a broad
   government/royal greeting default. Merged guidance instead matches audience and
   source intent, avoids guessed gender/kinship, and distinguishes rank-specific forms.
5. kien-thai excludes chat and UI strings, mandates model routing during its workflow,
   and its kode-thai loop has no pass limit. The new core includes comprehension, chat
   and UI, uses the current model, offers compact teaching examples, and caps optional
   deep editing at three passes. Scripts requiring optional native models/corpus paths
   are not runtime dependencies or shipped as automatic routing.
6. Strong stylistic claims in kien-thai are register preferences rather than universal
   grammar. The merged core allows legitimate passive forms, connective words and
   summaries, and prioritizes factual fidelity over invented specificity. It explains
   that advanced upstream material is optional and that the core overrides categorical
   bans. Constructed examples are clearly labeled; no claim that they are native corpus.

7. Hermes profiles can inherit an external skills directory. Installing the same names
   into both local and inherited directories causes the runtime to reject ambiguous
   names, even though `skills list` shows them as enabled. Removed only our owned
   profile-local copies; named-profile now inherits the root installation. The safe uninstaller
   checks receipt hashes before deleting and preserves unrelated content.

8. Removed the twelve nested single-skill plugin manifests inherited from Boom-Vitt.
   The package now has one Claude plugin entrypoint, avoiding accidental standalone
   plugin registration when skills are copied into a harness directory.

## What was preserved

Twelve domain skills and their utility code/templates, domain disclaimers, upstream MIT
notices, and selected author-written kien-thai references. The core adds meanings of
Thai negation, implicit subjects, qualified requests, mixed-language text, modality,
neutral voice, and factual checks. Installer copies content with provenance receipts,
protects conflicting or modified files, and accepts arbitrary skill directories.

## Review limits

Ran the upstream utility suite (8 test files) and kien-thai's default suite (53 passed,
1 skipped, 21 deselected). Inspected skill packaging, language entrypoints, supporting
references, routing dependencies, installer behavior and date utilities. Added seven
regression tests plus TypeScript calendar/era checks.

This was not a full legal, tax, royal-vocabulary or postal-database correctness audit.
The inherited domain material includes jurisdiction-dependent rules and approximate
address/ID checks; its own limitations still apply. A checksum proves only internal
consistency, not that an ID is issued. Keep issuer-provided data unchanged, confirm
current domain requirements when needed, and do not treat drafting templates as an
independent authority. The prose smoke tasks are small, not a Thai quality benchmark.
