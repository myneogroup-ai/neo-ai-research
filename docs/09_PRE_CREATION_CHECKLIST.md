# Pre-creation checklist

Everything to settle **before** `gh repo create` runs. The items are ordered by how much
more expensive they become after the repository exists, most expensive first.

Nothing here is a formality. Four of these items cannot be fixed later at any price.

---

## A. Irreversible after the repository is public

| # | Item | Why it cannot be fixed later | Done |
|---|---|---|---|
| A1 | **Read the whole tree.** Every file, not a sample | Making a repository public publishes its full history. A file deleted in a later commit is still in the history, and in every fork and clone | ☐ |
| A2 | **No credential, token or key anywhere in the tree or the intended history** | A published secret is a compromised secret. Rotation is the only remedy and it is not a remedy for what was read | ☐ |
| A3 | **Confirm every file against `docs/07_CLASSIFICATION_POLICY.md`** | A disclosure cannot be undone by removing the page | ☐ |
| A4 | **Create the repository PRIVATE.** Make it public only after the first conformance run is green and a person has read the tree | This is the whole point of A1 to A3. A repository created public is public from its first second | ☐ |

## B. Frozen at first publication, therefore free now and expensive later

| # | Item | Note | Done |
|---|---|---|---|
| B1 | **Settle the category slug for institutional publications.** Two terminal artefacts disagree: the machine-readable register says `institutional`, one prose map says `publications`. This repository follows the register | A slug is frozen at first publication. Changing it now is a one-line edit; changing it after publication breaks every citation and requires a permanent redirect | ☐ |
| B2 | **Confirm every other slug in `registers/publications.json`** | Same reason. Read all nine | ☐ |
| B3 | **Confirm the route template** `/research/{category}/{slug}/` | Every canonical URL derives from it | ☐ |
| B4 | **Confirm the identifier route** `/id/<PUBID>`, `302` | Every external citation goes through it | ☐ |
| B5 | **Register an ORCID for the author** | Required before first publication. It appears on the `Person` node and on every article's author reference, and adding it later means every published page's markup was incomplete | ☐ |

## C. Must exist before the first push, or a control is silently not enforced

| # | Item | If missing | Done |
|---|---|---|---|
| C1 | GitHub organisation `myneogroup-ai` exists | Nothing works | ☐ |
| C2 | Teams exist: `research-maintainers`, `research-program`, `editorial`, `platform`, `security`, `legal` | **A `CODEOWNERS` rule naming a team that does not exist is silently not enforced.** The file looks correct and reviews nothing | ☐ |
| C3 | Every team has at least one member | A required review from an empty team blocks every pull request | ☐ |
| C4 | `security@myneogroup.com` and `conduct@myneogroup.com` are monitored inboxes | `SECURITY.md` and `CODE_OF_CONDUCT.md` both direct people to them | ☐ |
| C5 | Commit signing configured for every maintainer | Branch protection requires signed commits, and turning that on afterwards is a migration | ☐ |
| C6 | Private vulnerability reporting enabled | `SECURITY.md` tells people to use it | ☐ |
| C7 | Secret scanning **with push protection** enabled | Push protection blocks the commit. Secret scanning alone reports it after the fact | ☐ |

## D. Governance state, not repository state

| # | Item | Blocks | Done |
|---|---|---|---|
| D1 | The canonical-host amendment is **signed** | Every canonical URL in the repository is correct on signature and not before | ☐ |
| D2 | The vocabulary amendment is **signed** | `registers/vocabulary.json` carries 39 terms on signature and 30 before it | ☐ |
| D3 | The capability register is **ratified** | Until then every page must render it as provisional, and `verify_public.py` check `REG-10` enforces that it still says so | ☐ |
| D4 | The R-009 identifier is **allocated** | Until then the paper is cited by title, `citation_technical_report_number` is omitted, and the library index says "not yet allocated" | ☐ |
| D5 | Prepared edits applied to P-001, P-007, TN-001, TN-002, TN-003 | Five of the six Wave 1 documents. Until then their `_PENDING_IMPORT.md` files remain and `--strict` blocks any release | ☐ |
| D6 | The glossary is reduced to a public term set | Term pages, the glossary sitemap and first-occurrence linking all wait on it | ☐ |
| D7 | The four non-blocking open governance items are ruled | Named in the release documentation | ☐ |

**D1 to D7 do not block creating the repository.** They block releasing from it, and
`verify_public.py --strict` is what enforces that: every declared deferral in
`scripts/known_deferrals.json` names the step that clears it, and the release workflow
treats an outstanding deferral as a failure.

## E. Deployment, before the first deploy rather than before creation

| # | Item | Done |
|---|---|---|
| E1 | Hosting configured for both hosts, static, server-rendered HTML | ☐ |
| E2 | Staging host: `noindex` on every response, HTTP authentication, no sitemap submitted | ☐ |
| E3 | GitHub Environments created: `staging`, `production-phase-a`, `production-phase-b` | ☐ |
| E4 | Required reviewers set on **both** production environments and on neither staging nor rollback | ☐ |
| E5 | Deployment credentials in Environment secrets. **Never in the repository** | ☐ |
| E6 | Rollback rehearsed in staging and **timed under 30 minutes** | ☐ |
| E7 | Both executing officers named, and reachable | ☐ |
| E8 | Analytics baseline captured: 28 days of organic entrances, and the indexed URL count | ☐ |

E8 is easy to skip and cannot be reconstructed afterwards. Two of the rollback triggers are
measured against a baseline that has to exist before the change.

## F. Read once, before the first push

| # | Document | Done |
|---|---|---|
| F1 | `docs/07_CLASSIFICATION_POLICY.md`, in full | ☐ |
| F2 | `docs/06_CANONICAL_URL_MAP.md`, section 5 in particular | ☐ |
| F3 | `docs/05_ROLLBACK.md`, especially that rollback needs no approval | ☐ |
| F4 | `SECURITY.md`, and confirm the reporting channels work | ☐ |

---

## The four that cannot be fixed later, at any price

1. **A published secret.** Rotation is the only remedy, and it does not remedy what was
   read.
2. **A published classified passage.** Removing the page limits further exposure. It does
   not undo the exposure.
3. **A pinned version redirected forward.** It silently falsifies the citation record and
   no rollback recovers it.
4. **An external citation of a URL made during a window you later reverse.** This is the
   entire reason phase D waits seven days behind phase B.

Everything else on this page is recoverable. These four are not.

---

## Sign-off

| | |
|---|---|
| Sections A to F complete | ☐ |
| Repository created private on | ________________ |
| First conformance run green on | ________________ |
| Tree read in full by | ________________________________________ |
| Made public on | ________________ |
| Made public by | ________________________________________ |
