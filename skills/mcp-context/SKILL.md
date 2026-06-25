---
name: mcp-context
description: Use when a task needs to connect an assistant to the Intelligems MCP server, choose MCP tools, resolve organization context, or apply Intelligems MCP safety boundaries.
license: MIT
---

# Intelligems MCP Context

Use this as the shared context layer for Intelligems MCP tasks.

## First Moves

1. Confirm the user's objective: analysis, reporting, integration, or live experience management.
2. Confirm the Intelligems organization if the user has access to more than one. Prefer the current tool name exposed by the client, usually `list_organizations`; some setup docs refer to `getOrganizationsList`.
3. Use read-only tools first. Do not create, update, start, pause, or end experiences without explicit approval for the exact organization, experience, action, and payload.
4. State the data boundary in the answer: organization, date range, experience IDs, analytics view, and whether results came from MCP, External API, or both.

## Hosted MCP Endpoint

The hosted Intelligems MCP server is available at:

```text
https://ai.intelligems.io/mcp
```

SSE fallback:

```text
https://ai.intelligems.io/mcp/sse
```

## Core Tool Groups

Use the exact tool names exposed in the current client. Current public docs include:

- Organization and configuration: `list_organizations`, `get_organization`, `switch_organization`, `list_integrations`.
- Experiences and experiments: `search_experiences`, `search_experiments`, `search_personalizations`, `list_experiments`, `list_personalizations`, `get_experience`, `get_experience_metrics_config`, `analyze_experience`.
- Mutating experience tools: `create_experience`, `update_experience`, `experience_action`.
- Shopify store data: `search_products`, `list_collections`, `list_pages`, `search_policies`.
- Analytics and audience data: `get_sitewide_analytics`, `get_audience_by_country`, `get_audience_by_device`, `get_audience_by_visitor_type`, `get_audience_by_source_channel`, `get_audience_by_source_site`, `get_audience_by_landing_page`.
- Visualization: `generate_intelligems_graph`, `generate_custom_graph`.
- Custom events and offers: `list_custom_events`, `list_offers`.

## Answer Discipline

- Separate observed results from recommendations.
- Never invent statistical significance, lift, confidence, visitor counts, RPV, GPV, or revenue impact.
- If a required metric is unavailable, say what is missing and provide the safest next query.
- Prefer profit metrics when available. Conversion rate alone is not enough to call a winner.
- Mention any caveats around sample size, date range, audience split, or partially complete tests.
- Treat returned exports, graph URLs, order-level data, and raw API responses as private unless the user explicitly says they are synthetic or public.

## References

Load `references/intelligems-mcp.md` when you need detailed endpoint, tool, or doc-source context.
