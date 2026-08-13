# Git commands, in order

Every command that touches a remote is listed. Nothing here is run without the
corresponding authorisation being in place first.

## 1. Create the repository

Settle `docs/09_PRE_CREATION_CHECKLIST.md` before running any of this. Several of the
decisions in it are far cheaper before the repository exists than after.

```bash
# The organisation and its teams must exist first. The teams are referenced by
# .github/CODEOWNERS and a code-owner rule naming a team that does not exist is silently
# not enforced.
gh api -X POST orgs/myneogroup-ai/teams -f name='research-maintainers' -f privacy=closed
gh api -X POST orgs/myneogroup-ai/teams -f name='research-program'     -f privacy=closed
gh api -X POST orgs/myneogroup-ai/teams -f name='editorial'            -f privacy=closed
gh api -X POST orgs/myneogroup-ai/teams -f name='platform'             -f privacy=closed
gh api -X POST orgs/myneogroup-ai/teams -f name='security'             -f privacy=closed
gh api -X POST orgs/myneogroup-ai/teams -f name='legal'                -f privacy=closed

# Create it PRIVATE. It is made public only after the first conformance run passes and a
# human has read the tree. A repository created public is public from its first second,
# including anything committed by mistake in the first push.
gh repo create myneogroup-ai/neo-ai-research \
  --private \
  --description "The public research corpus of the NEO AI Research Program" \
  --homepage "https://neoai.myneogroup.com/research/"
```

## 2. First push

```bash
cd neo-ai-research
git init -b main
git config user.signingkey <KEY>
git config commit.gpgsign true

# Read the tree before the first commit. This is the last cheap moment to find something
# that should not be there.
python3 scripts/verify_public.py --self-test
python3 scripts/verify_public.py
python3 scripts/build_indexes.py --check
python3 scripts/gen_seo.py --check

git add -A
git status            # read it, do not skim it
git commit -S -m "chore: initialise the public research repository

Governance files, CI, discovery generators and workflow documentation.
Four public research texts. No publication is deployed by this commit."

git remote add origin git@github.com:myneogroup-ai/neo-ai-research.git
git push -u origin main
```

## 3. Configure, while still private

```bash
gh api -X PUT repos/myneogroup-ai/neo-ai-research/branches/main/protection \
  --input .github/branch-protection.json

gh api -X PATCH repos/myneogroup-ai/neo-ai-research \
  -F has_issues=true -F has_wiki=false -F has_projects=false \
  -F allow_squash_merge=true -F allow_merge_commit=false -F allow_rebase_merge=false \
  -F delete_branch_on_merge=true -F allow_auto_merge=true

# Private vulnerability reporting. SECURITY.md tells people to use it, so it must exist.
gh api -X PUT repos/myneogroup-ai/neo-ai-research/private-vulnerability-reporting

# Secret scanning and push protection. Push protection is the one that matters: it stops
# the commit rather than reporting it afterwards.
gh api -X PATCH repos/myneogroup-ai/neo-ai-research \
  -f 'security_and_analysis[secret_scanning][status]=enabled' \
  -f 'security_and_analysis[secret_scanning_push_protection][status]=enabled'

# Environments. The two production environments carry required reviewers; staging does
# not. Rollback deliberately targets no environment at all.
gh api -X PUT repos/myneogroup-ai/neo-ai-research/environments/staging
gh api -X PUT repos/myneogroup-ai/neo-ai-research/environments/production-phase-a \
  -F 'reviewers[][type]=Team' -F 'reviewers[][id]=<RESEARCH_MAINTAINERS_TEAM_ID>'
gh api -X PUT repos/myneogroup-ai/neo-ai-research/environments/production-phase-b \
  -F 'reviewers[][type]=Team' -F 'reviewers[][id]=<RESEARCH_MAINTAINERS_TEAM_ID>'

gh workflow run labels.yml
```

## 4. Make it public

Only after the first conformance run is green and a person has read the tree.

```bash
gh api -X PATCH repos/myneogroup-ai/neo-ai-research -F private=false
```

**This is the irreversible step in this document.** Everything before it can be deleted
without consequence. After it, assume the tree and its full history have been cloned.

## 5. Day to day

```bash
git switch main && git pull --ff-only
git switch -c content/p-007-responsible-capability-claims

# ... work ...
python3 scripts/verify_public.py
python3 scripts/build_indexes.py && python3 scripts/gen_seo.py

git add -A
git commit -S -m "content(P-007): add A Note on Responsible AI Capability Claims v1.0"
git push -u origin HEAD
gh pr create --fill --base main
```

## 6. Cut a release

```bash
git switch main && git pull --ff-only
python3 scripts/verify_public.py --strict     # every deferral counts as a failure here

# Update CHANGELOG.md first. The gate fails without an entry for the tag.
git tag -s corpus-v1.0.0 -m "Corpus v1.0.0: Public Wave 1"
git push origin corpus-v1.0.0                  # this fires .github/workflows/release.yml
```

## 7. Deploy

Deployment is never a git command. It is a workflow dispatch carrying a signed
authorisation reference, and it stops at an environment approval.

```bash
gh workflow run deploy.yml \
  -f target=staging -f site=both -f authorisation="<REFERENCE>"

# Rehearse the rollback and record the time before going further. Over thirty minutes
# holds publication.

gh workflow run deploy.yml \
  -f target=production-phase-a -f site=neoai -f authorisation="<REFERENCE>"
gh workflow run deploy.yml \
  -f target=production-phase-b -f site=both  -f authorisation="<REFERENCE>"
```

## 8. Roll back

No approval. No ceremony. Inform afterwards.

```bash
gh workflow run rollback.yml \
  -f trigger="T7 classified material on a public page" \
  -f scope="revert the build, phase B" \
  -f ref=corpus-v1.0.0
```

## Commands that must never be run

```bash
git push --force origin main          # history is a provenance claim
git tag -d corpus-v1.0.0              # a tag that moves breaks everybody who pinned to it
git push --delete origin corpus-v1.0.0
```

If something must be removed from history, that is a security incident under
`SECURITY.md` and not a git operation somebody performs alone.
