# Distribution

This repository is a public Agent Skills package. It is intended to be installed from GitHub with Vercel's open `skills` CLI.

## Recommended Install

List available skills:

```bash
npx skills add intelligems-io/intelligems-mcp-skills --list
```

Install the package interactively:

```bash
npx skills add intelligems-io/intelligems-mcp-skills
```

Install one skill:

```bash
npx skills add intelligems-io/intelligems-mcp-skills --skill profit-growth-audit
```

Install all skills:

```bash
npx skills add intelligems-io/intelligems-mcp-skills --all
```

Install for a specific supported agent:

```bash
npx skills add intelligems-io/intelligems-mcp-skills --skill weekly-test-pulse -a claude-code
npx skills add intelligems-io/intelligems-mcp-skills --skill weekly-test-pulse -a codex
```

Install globally:

```bash
npx skills add -g intelligems-io/intelligems-mcp-skills --skill weekly-test-pulse
```

Use without installing:

```bash
npx skills use intelligems-io/intelligems-mcp-skills --skill weekly-test-pulse
```

## Updates

Check for updates:

```bash
npx skills check
```

Apply updates:

```bash
npx skills update
```

## skills.sh

There is no separate publish command for skills.sh. A public GitHub repository can be installed directly. Public packages can become discoverable through the skills ecosystem as people install them with the `skills` CLI.

## Vercel MCP Deployment

Vercel's MCP deployment docs are for teams that want to host their own MCP servers. This repository does not host an MCP server. Intelligems already hosts the MCP server at:

```text
https://ai.intelligems.io/mcp
```

This repository only packages reusable agent instructions for working with that server and the External API.

## Claude Code Plugin Marketplace

Claude Code also supports plugin marketplaces. This repository currently publishes plain Agent Skills because that is the most portable format across Codex, Claude Code, Cursor, and other skills-compatible agents.

If a future release needs hooks, commands, bundled MCP configuration, or a richer Claude-only install surface, create a separate Claude Code plugin package instead of mixing plugin-only behavior into these portable skills.
