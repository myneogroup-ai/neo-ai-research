# Wave 1 publication readiness (2026-11-17)

The Founder approved the publication of Wave 1 on `neoai.myneogroup.com` on 2026-11-17. Approval starts the
procedure of `03_PUBLICATION_WORKFLOW.md` and `04_DEPLOYMENT.md`; it does not replace its signatures and readings.
This page lists, item by item, what is done (with its evidence), what an agent builds, and what only a named person
can do. Source of the items: `09_PRE_CREATION_CHECKLIST.md`.

## 1. Done, with evidence

| Item | Evidence |
|---|---|
| Automated conformance | `make release` on 2026-11-17: `verify_public --strict` 0 findings, 7 generated indexes current, 19 discovery files current |
| D3 capability register ratified | v1.3 2026-08-13, v2.0 2026-10-18 (checklist) |
| D4 R-009 identifier allocated | checklist |
| D5 prepared edits applied | no `*_PENDING_IMPORT.md` file remains outside the glossary backlog (`--strict` passes) |
| Security scanning | gitleaks and Semgrep on every push (`12_SECURITY_SCANNING.md`) |
| Six documents marked `APPROVED_FOR_WAVE_1` | `registers/publications.json`: P-001, P-007, R-009, TN-001, TN-002, TN-003 (R-001, R-003, R-005 held for Wave 1B) |

## 2. Built by an agent (no signature needed, nothing goes public)

| Item | Work | State |
|---|---|---|
| Rendered HTML | `scripts/build_site.py` (`make preview`, `make site`, `make site-check`): static, server-rendered HTML of the six Wave 1 documents, the methodology and the register pages; held documents are never rendered; the production build carries the `/id/<PUBID>` 302 resolver | BUILT 2026-11-17 (`site-check` OK) |
| E2 staging | Private reading copy for the gate B and gate C readers: a private Claude artifact, owner-only until the Founder shares it with a named reader, `noindex` and a PREVIEW banner on every page. A staging host with HTTP authentication remains to be set up for the rollback rehearsal (E6) | PREVIEW BUILT 2026-11-17 |
| E1 hosting | Phase A on the live host: the research pages and the `/id/<PUBID>` resolver added to the `neoai.myneogroup.com` site through its own repository (`myneogroup-websites`, `deploy-neoai.yml`) | TO BUILD after gates B and C |
| E6 rollback rehearsal | Timed in staging, must be under 30 minutes | TO DO in staging |
| D6 glossary reduced to a public term set | A proposal of the public terms, for the Founder's approval | TO DRAFT |

## 3. Only a named person can do these

| Item | Who | What exactly |
|---|---|---|
| Gate B, one per document | A named reviewer who is NOT the author (the author is the Founder) | Reads each of the six documents against the five questions of `03_PUBLICATION_WORKFLOW.md` section 6 and signs one sheet per document |
| Gate C, adversarial read | A person who never worked on the corpus | Reads the staging site and answers: "Does this read as a description of a system that exists?" Yes stops the release |
| B1 to B4 | Founder | Confirms the slugs, the route template `/research/{category}/{slug}/` and the identifier route `/id/<PUBID>` (302). Frozen at first publication |
| B5 | Founder | Registers an ORCID (https://orcid.org/register) and gives the number |
| D1, D2 | Founder | Signs the canonical-host amendment and the vocabulary amendments |
| D7 | Founder | Rules the four open governance items |
| E3, E4 | Founder (GitHub settings) | Creates the environments `staging`, `production-phase-a`, `production-phase-b` with required reviewers on the two production ones |
| E7 | Founder | Names the two executing officers |
| Publication authorisation, part 1 | Founder, signed | Reference given to the deploy workflow for phases A and B |

## 4. Order

1. Agent: rendered build and private staging; glossary proposal.
2. Founder: B1 to B5, D1, D2, D7, names for gate B, gate C and the two officers.
3. Readers: gate B sheets, then gate C on staging.
4. Agent: rollback rehearsal in staging (timed); Founder: environments E3 and E4.
5. Founder signs publication authorisation part 1; phase A (live, unlinked), then phase B (the publication moment).
6. Phase D (redirects) not before seven days after B, under authorisation part 2.

## 5. What this page does not claim

No date is promised: gates B and C depend on people. The live site's `/research/` currently redirects to GitHub and
`/id/<PUBID>` answers 404; the weekly identifier-route check stays red until phase A.
