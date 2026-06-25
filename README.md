# Intelligems MCP Skills

Open Agent Skills for [Intelligems](https://www.intelligems.io/), the ecommerce experimentation, personalization, and price-testing platform. Give your AI agent a proven workflow instead of writing prompts from scratch.

Built for connected operators and ecommerce teams who want agents to:

- Analyze test results and surface what actually moved.
- Catch profit traps where conversion gains hide margin loss.
- Review client or program performance without rebuilding prompts.
- Study segments, pricing response, and testing roadmaps.

How it works:

- Install a skill with one command.
- Connect your own Intelligems account.
- Your agent runs the workflow through the MCP server or External API.
- The skills supply the method; you bring the data.

Data safety:

- Public instructions only, no API keys, tokens, or customer data.
- Skills start read-only, so your agent reads and reports before changing anything.

## What's Inside

- `skills/mcp-context` - shared context for the hosted Intelligems MCP server.
- `skills/profit-growth-audit` - profit-focused audit flow, linked to the official public audit repo.
- `skills/weekly-test-pulse` - quick status readout for running tests.
- `skills/client-performance-review` - monthly review workflow for agencies and customer-facing teams.
- `skills/profit-trap-detection` - finds tests where conversion gains may hide profit loss.
- `skills/segment-intelligence` - audience-segment analysis across tests.
- `skills/test-roadmap` - quarterly roadmap planning from historical testing data.
- `skills/testing-strategy-health-check` - program health review for velocity, win rate, and coverage.
- `skills/price-sensitivity-analysis` - price and discount response analysis.
- `skills/api-integration-builder` - External API patterns for dashboards, alerts, and automations.

See `CATALOG.md` for the full skill map.

## Install

The friendly install path is Vercel's open `skills` CLI:

```bash
npx skills add intelligems-io/intelligems-mcp-skills
```

List the available skills before installing:

```bash
npx skills add intelligems-io/intelligems-mcp-skills --list
```

Install one skill:

```bash
npx skills add intelligems-io/intelligems-mcp-skills --skill profit-growth-audit
```

Install for a specific agent:

```bash
npx skills add intelligems-io/intelligems-mcp-skills --skill weekly-test-pulse -a claude-code
npx skills add intelligems-io/intelligems-mcp-skills --skill weekly-test-pulse -a codex
```

Install globally:

```bash
npx skills add -g intelligems-io/intelligems-mcp-skills --skill profit-growth-audit
```

Use a skill once without installing it:

```bash
npx skills use intelligems-io/intelligems-mcp-skills --skill profit-growth-audit
```

Manual copying still works as a fallback. A skill is the folder that contains `SKILL.md`, plus optional `references/`, `scripts/`, and `assets/`.

## Connect The MCP Server

The skills teach agents how to use Intelligems. They do not authenticate users or include credentials.

To use live Intelligems data, connect your AI client to the hosted Intelligems MCP server with your own Intelligems account. For Claude Code, the public Intelligems docs show:

```bash
claude mcp add --transport http intelligems https://ai.intelligems.io/mcp
```

Hosted MCP endpoint:

```text
https://ai.intelligems.io/mcp
```

SSE fallback:

```text
https://ai.intelligems.io/mcp/sse
```

Vercel also documents how to host MCP servers, but this repository is not an MCP server deployment. Intelligems already hosts the MCP server. This repository is a skill package that can be installed by agents.

## Updates & Sharing

- Install from GitHub with `npx skills add intelligems-io/intelligems-mcp-skills`.
- No npm token or registry publishing step is required.
- There is no separate skills.sh publish command. Public repositories can become discoverable as people install them through the skills CLI.
- See `DISTRIBUTION.md` for installation, update, and optional marketplace notes.

## References

The skill instructions are grounded in these public resources:

- Intelligems MCP docs: https://docs.intelligems.io/developer-resources/mcp-server
- Intelligems MCP available tools: https://docs.intelligems.io/developer-resources/mcp-server/available-tools
- Intelligems MCP examples and best practices: https://docs.intelligems.io/developer-resources/mcp-server/examples-and-best-practices
- Intelligems External API docs: https://docs.intelligems.io/developer-resources/external-api
- Intelligems OpenAPI spec: https://static.intelligems.io/api-docs-v25-10-prod.json
- Agent Skills standard: https://agentskills.io/specification
- Vercel skills CLI: https://github.com/vercel-labs/skills
- Claude Code skill docs: https://code.claude.com/docs/en/skills
- Codex Agent Skills docs: https://developers.openai.com/codex/skills

## Data & Security

Skills lead with read-only MCP and API calls. Creating, updating, starting, pausing, ending, or exporting an Intelligems experience requires explicit approval for that exact action.

For contributors: do not commit API keys, access tokens, customer data exports, order-level exports, presigned download URLs, screenshots with secrets, or private brand data.

The validation script checks skill format plus common secret and private-context patterns:

```bash
python3 scripts/validate_skills.py
```
