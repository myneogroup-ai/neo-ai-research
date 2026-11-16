# 12 - Security scanning

Every pull request and every push to a branch other than `main` runs `.github/workflows/security-scan.yml`, which
deploys nothing:

- **gitleaks** (secrets), version pinned and checksum-verified. Reviewed false positives are listed in
  `.gitleaks.toml` with their review date and reason (today: the capability identifiers `"key": "x100.*"` of the
  capability register). A real credential found by the scan is rotated first, then removed.
- **Semgrep OSS** (static analysis, rule packs `p/default` and `p/secrets`). ERROR findings fail the check; the full
  list of findings of a run is the `semgrep report` check run.

The first full scan (2026-11-15) found six command-injection paths in the deployment, release and rollback workflows:
dispatch inputs reached shell code inline. They now reach the scripts as environment variables only.
