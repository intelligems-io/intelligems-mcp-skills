# Public Security Review

Use this checklist before publishing changes to this repository.

## Must Not Be Present

- API keys, OAuth tokens, MCP session tokens, or GitHub tokens.
- Customer exports, order-level CSVs, line-item CSVs, or raw private analytics responses.
- Presigned download URLs or generated graph URLs from real accounts.
- Screenshots, logs, reports, or copied dashboard content from real customer accounts.
- Store domains, customer emails, order IDs, visitor IDs, organization IDs, or experience IDs from private accounts.
- Internal messages, tickets, meeting notes, or private source material.

## Allowed

- Public documentation links.
- General workflow instructions.
- Clearly fake placeholders like `YOUR_EXPERIENCE_ID`.
- Source-backed MCP and API capability summaries.
- Validation scripts that do not require secrets.

## Required Checks

Run:

```bash
python3 scripts/validate_skills.py
git diff --check
LC_ALL=C rg -n "[^\x00-\x7F]" . || true
```

Also run a skills CLI smoke test from a temporary directory:

```bash
npx skills add intelligems-io/intelligems-mcp-skills --list
```

For local, unpublished changes:

```bash
npx skills add /absolute/path/to/intelligems-mcp-skills --list
```

## Human Review

Before publishing, skim `README.md`, `SOURCES.md`, `SECURITY.md`, `DISTRIBUTION.md`, every `SKILL.md`, and all `references/` files. If any content would help someone infer private customer performance, store identity, credentials, or internal operating context, remove it.
