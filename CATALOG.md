# Skill Catalog

Each folder under `skills/` is a portable Agent Skill with a `SKILL.md` entrypoint.

| Skill | Use When | Primary Sources |
| --- | --- | --- |
| `mcp-context` | Any Intelligems MCP task needs shared setup, organization handling, or safety boundaries. | MCP docs, available tools, examples |
| `profit-growth-audit` | A user asks for a profit-focused CRO or testing audit. | Official `intelligems-io/profit-growth-audit`, MCP docs |
| `weekly-test-pulse` | A user wants a concise status report on currently running tests. | MCP examples, available tools |
| `client-performance-review` | A user needs a monthly client or account performance review from completed tests. | MCP examples, available tools |
| `profit-trap-detection` | A user wants to catch tests where conversion rate improved but RPV or GPV declined. | MCP examples, analytics tools |
| `segment-intelligence` | A user wants customer, device, geography, landing-page, or traffic-source breakdowns. | MCP audience tools |
| `test-roadmap` | A user wants a quarterly testing roadmap or next-best-test plan. | MCP examples, historical experiment analysis |
| `testing-strategy-health-check` | A user wants to assess testing program velocity, win rate, test mix, or gaps. | MCP examples, experience search |
| `price-sensitivity-analysis` | A user wants price or discount response analysis from test results. | MCP examples, analytics tools |
| `api-integration-builder` | A user wants scripts, dashboards, alerts, or pipelines using the External API. | External API docs, OpenAPI spec |

## Compatibility

The skills use the portable `SKILL.md` layout described by the Agent Skills standard and Claude Code docs. They are intentionally plain Markdown so they can be copied into Codex, Claude Code, or another compatible agent runtime.

## Shared Resource Pattern

Most task skills instruct the agent to load `skills/mcp-context/references/intelligems-mcp.md` when it needs detailed tool context. This keeps each skill small while preserving the source-backed reference.
