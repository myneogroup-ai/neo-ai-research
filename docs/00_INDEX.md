# Repository documentation

| # | Document | Answers |
|---|---|---|
| 01 | `01_BRANCH_STRATEGY.md` | Which branch, named how, protected how |
| 02 | `02_RELEASE_STRATEGY.md` | Versioning, tags, what a release is and is not |
| 03 | `03_PUBLICATION_WORKFLOW.md` | How a document becomes a published page |
| 04 | `04_DEPLOYMENT.md` | How a build reaches a public host |
| 05 | `05_ROLLBACK.md` | How it is undone, and by whom, without asking |
| 06 | `06_CANONICAL_URL_MAP.md` | Every route on both hosts, and who is canonical for what |
| 07 | `07_CLASSIFICATION_POLICY.md` | What may be published and what may not |
| 08 | `08_GIT_COMMANDS.md` | The exact commands, in order |
| 09 | `09_PRE_CREATION_CHECKLIST.md` | Everything to settle before the repository exists |
| 10 | `10_SEO_AND_DISCOVERY.md` | Sitemaps, robots, feeds, `llms.txt`, crawler policy |
| 11 | `11_STRUCTURED_DATA.md` | The entity graph and the no-overclaim rule |

Three of these are worth reading before touching anything: **07**, because publishing the
wrong thing is the only failure here that cannot be undone; **06**, because a URL decision
made carelessly is expensive to reverse; and **09**, because several decisions in it are
much cheaper before the repository exists than after.
