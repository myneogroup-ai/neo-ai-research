# Security and disclosure policy

This repository holds published research and the code that builds a public website from
it. It runs no service and processes no user data. The security surface is therefore
narrower than a product repository and one category of report matters far more than the
rest.

## The report we most want to receive

**Classified material published in error.** If you believe a page, a file, a commit, a
branch or a git history entry in this repository or on either public host contains
material that should not be public, report it privately and immediately.

Examples of what this means in practice:

- An internal service name, component contract, schema or deployment topology
- A numeric threshold, coefficient, weight or objective function
- An evaluation denominator, gate rule or benchmark dataset
- The name of a pilot client, a contract value or any financial figure
- An internal file path, hostname, ticket reference or repository name
- A credential, token or key of any kind

**Do not open a public issue for this.** A public issue describing where the disclosure
is amplifies it.

## How to report

| Channel | Use |
|---|---|
| GitHub private vulnerability reporting, Security tab, "Report a vulnerability" | Preferred for everything |
| `security@myneogroup.com` | If private reporting is unavailable to you |

Please include the file or URL, the commit if you know it, and what you believe is
disclosed. You do not need to be certain. A report that turns out to be a false alarm
costs us an hour; an unreported disclosure costs more.

## What happens next

| Stage | Target |
|---|---|
| Acknowledgement | 2 business days |
| Initial assessment | 5 business days |
| Withdrawal of an affected public page, if the report is confirmed | Same day as confirmation |
| Resolution or a stated plan | 30 days |

A confirmed disclosure triggers the withdrawal path in `docs/05_ROLLBACK.md`. Removing a
page limits further exposure; it does not undo the exposure that has already happened, and
the handling of that is separate from this repository.

## In scope

- Classified material in the repository, its history or on either public host
- Credentials or tokens committed to the repository
- A workflow that could be made to run untrusted code or exfiltrate a secret
- Supply-chain risk in a pinned action or dependency
- A vulnerability in the generated static site: injection through content, an unsafe
  redirect, a header misconfiguration

## Out of scope

- Findings against third-party hosting or CDN infrastructure, which belong to those
  vendors
- Missing headers with no demonstrated impact on a static site
- Automated scanner output with no analysis attached
- Disagreement with a research position. That is an issue, and it is welcome as one

## Safe harbour

We will not pursue or support action against anyone who reports in good faith through the
channels above, avoids privacy violations and service disruption, and gives us reasonable
time to respond before disclosing publicly.

## Credentials

This repository should contain no secret of any kind. Deployment credentials live in
GitHub Environments with required reviewers, never in the repository, never in a workflow
file, never in a commit message. If you find one, treat it as a confirmed report under the
process above.
