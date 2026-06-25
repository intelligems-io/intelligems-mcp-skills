---
name: segment-intelligence
description: Use when a user asks how Intelligems test performance differs by device, visitor type, country, traffic source, source site, or landing page.
license: MIT
---

# Segment Intelligence

Use this skill to identify customer segments that consistently overperform or underperform.

## Segment Tools

Current public MCP docs include:

- `get_audience_by_country`
- `get_audience_by_device`
- `get_audience_by_visitor_type`
- `get_audience_by_source_channel`
- `get_audience_by_source_site`
- `get_audience_by_landing_page`

You can also use `analyze_experience` with `view: "audience"` and the appropriate audience field when the active client exposes that path.

## Steps

1. Resolve organization, experience scope, and date range.
2. Identify relevant tests with `search_experiences`, `search_experiments`, or explicit experience IDs from the user.
3. Pull overview metrics first so segment findings have context.
4. Pull only the segment dimensions needed for the user question.
5. Compare segment behavior across tests to separate one-off noise from repeated patterns.

## Output

Return:

1. Strongest segment insights.
2. Segment table with metric direction, confidence, and sample caveats.
3. Segment-specific recommendations.
4. Tests to run next if the pattern is actionable.
5. Appendix with dimensions queried, tool calls, and any missing metrics.

Do not overstate tiny segments. If sample size is thin, label the finding as directional.

## Data Safety

Use only the user's authenticated MCP or API context. Do not save raw responses, exports, graph URLs, order data, customer data, or private store identifiers to the repository. Summarize findings and include experience IDs only when needed for the user's workflow.
