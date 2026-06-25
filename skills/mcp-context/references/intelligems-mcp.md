# Intelligems MCP Reference

Sources:

- https://docs.intelligems.io/developer-resources/mcp-server
- https://docs.intelligems.io/developer-resources/mcp-server/available-tools
- https://docs.intelligems.io/developer-resources/mcp-server/examples-and-best-practices

Last checked: 2026-06-25.

## What It Provides

The Intelligems MCP server gives compatible AI clients authenticated access to Intelligems data and Shopify store information. Public docs list access to experiments and experiences, organization configuration, catalog and page data, analytics and audience data, custom events, offers, integrations, and chart generation.

The hosted server is operated by Intelligems. No local server install is required.

Recommended HTTP endpoint:

```text
https://ai.intelligems.io/mcp
```

SSE endpoint:

```text
https://ai.intelligems.io/mcp/sse
```

## Multi-Organization Handling

Most tools accept an optional `organization` parameter. Always specify it when the user has access to more than one organization or when the target store could be ambiguous.

Use `list_organizations` before analysis when the organization is unknown. The setup page also refers to `getOrganizationsList`; prefer the tool name exposed in the active client.

## Current Public Tool Categories

The public docs list 30 specialized tools:

Organization and configuration:

- `list_organizations`
- `get_organization`
- `switch_organization`
- `list_integrations`

Experiences and experiments:

- `search_experiences`
- `search_experiments`
- `search_personalizations`
- `list_experiments`
- `list_personalizations`
- `get_experience`
- `get_experience_metrics_config`
- `create_experience`
- `update_experience`
- `experience_action`
- `analyze_experience`

Shopify store data:

- `search_products`
- `list_collections`
- `list_pages`
- `search_policies`

Analytics and audience:

- `get_sitewide_analytics`
- `get_audience_by_country`
- `get_audience_by_device`
- `get_audience_by_visitor_type`
- `get_audience_by_source_channel`
- `get_audience_by_source_site`
- `get_audience_by_landing_page`

Visualization and charting:

- `generate_intelligems_graph`
- `generate_custom_graph`

Custom events and offers:

- `list_custom_events`
- `list_offers`

## Useful Read-Only Tool Paths

Discovery:

- `list_organizations`
- `get_organization`
- `list_integrations`
- `search_experiences`
- `search_experiments`
- `search_personalizations`
- `list_experiments`
- `list_personalizations`
- `get_experience`
- `get_experience_metrics_config`

Analysis:

- `analyze_experience`
- `get_sitewide_analytics`
- `get_audience_by_country`
- `get_audience_by_device`
- `get_audience_by_visitor_type`
- `get_audience_by_source_channel`
- `get_audience_by_source_site`
- `get_audience_by_landing_page`

Context:

- `search_products`
- `list_collections`
- `list_pages`
- `search_policies`
- `list_custom_events`
- `list_offers`

Visual output:

- `generate_intelligems_graph`
- `generate_custom_graph`

## Mutating Tools

Treat these as live-system actions:

- `create_experience`
- `update_experience`
- `experience_action`

Require exact user approval before using them. The approval must include organization, experience if applicable, action, and intended payload.

## Common Use Cases From Docs

Agencies:

- Monthly client performance review.
- Cross-test pattern analysis.
- Customer segment intelligence.
- Profit trap detection.
- Quarterly test roadmap.

Brand operators:

- Weekly test pulse check.
- Profit opportunity scan.
- Best customer segment analysis.
- Testing strategy health check.
- Price sensitivity analysis.

## Security Notes

Never share access tokens. The docs note that tokens can be scoped across all organizations a user can access, so compromised credentials should be revoked immediately.

Do not commit generated graph images, presigned URLs, raw analytics responses, order exports, line-item exports, organization IDs, or customer/store identifiers from real accounts.
