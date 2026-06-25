# Security

## Secrets

Never commit:

- Intelligems External API keys.
- OAuth tokens.
- MCP session tokens.
- GitHub tokens.
- Customer exports or raw private analytics data.
- Order-level or line-item-level exports.
- Presigned download URLs.
- Screenshots that expose credentials, private customer names, private store names, or private store data.
- API responses copied from real customer or brand accounts.
- Store domains, organization IDs, experience IDs, order IDs, visitor IDs, or customer emails from private accounts.

Use environment variables for local scripts:

```bash
export INTELLIGEMS_ACCESS_TOKEN="..."
```

Do not paste the value into Markdown, code, examples, or issue comments.

Use placeholders that are clearly fake:

- `$INTELLIGEMS_ACCESS_TOKEN`
- `YOUR_EXPERIENCE_ID`
- `YOUR_ORGANIZATION_ID`
- `example-store`

Do not use sample values that look like real client identifiers.

## MCP Boundaries

Start with read-only tools whenever possible:

- `list_organizations`
- `get_organization`
- `search_experiences`
- `list_experiments`
- `get_experience`
- `get_experience_metrics_config`
- `analyze_experience`
- `get_sitewide_analytics`
- audience breakdown tools

Require explicit approval before using mutating tools:

- `create_experience`
- `update_experience`
- `experience_action`

The approval must name the exact organization, experience, action, and intended payload.

Treat `generate_intelligems_graph`, `generate_custom_graph`, analytics exports, and any returned download URL as potentially sensitive. Do not commit generated artifacts or links unless they are created from public or synthetic data.

## External API Boundaries

GET and analytics POST requests are usually read-only, but they can return private data. Creating, updating, starting, pausing, ending, or exporting experiences changes live systems or exposes detailed data and requires explicit approval.

When using the External API:

- Read rate-limit headers and back off on `429`.
- Treat `401` as missing or invalid auth, not as a reason to ask for secrets in chat.
- Validate organization, experience ID, date range, and analytics view before producing recommendations.
- Store local responses outside the repository, or anonymize them before committing.
- Do not commit CSV exports, raw JSON responses, graph images, or generated reports from real accounts.

## Public Repository Rule

This repository is public. It should contain only:

- Public documentation links.
- General workflow instructions.
- Clearly fake placeholders.
- Source-backed MCP and API reference notes.
- Validation and security scripts that do not require secrets.

Anything copied from a private customer, brand, Slack message, ticket, dashboard, report, API response, or screenshot is out of scope for this repo.
