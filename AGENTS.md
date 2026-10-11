# Repository guidance

Read CONTRIBUTING.md before changing skills. Run `./scripts/test-all.sh` for
utility, installer or manifest changes. Packaging must use Git-tracked files;
never include local configuration, raw model outputs, secrets or symlinks.
Do not run live-model smoke tests automatically: they can consume provider quota.
Preserve upstream notices and source commits. Keep the two plugin manifests and
marketplace version aligned. Use constructed Thai examples and preserve factual
meaning during language edits.
