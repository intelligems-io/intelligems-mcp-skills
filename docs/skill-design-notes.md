# Skill Design Notes

This repo follows the portable Agent Skills pattern:

- Each skill is a directory with a `SKILL.md` entrypoint.
- `SKILL.md` starts with YAML frontmatter.
- `name` must match the parent directory name.
- `description` explains when the skill should load.
- `license` is set to `MIT` for public distribution.
- Long reference material lives in `references/` and is loaded only when needed.
- Skills give procedures and decision rules, not private data.

Claude Code docs recommend `SKILL.md` as the required entrypoint and note that supporting files can hold templates, examples, scripts, and reference documentation. The docs also describe frontmatter fields such as `name`, `description`, `when_to_use`, and `allowed-tools`.

The skills in this repo stay conservative:

- They ground analysis in MCP/API results.
- They identify source, organization, date range, and assumptions.
- They separate analysis from live-system mutation.
- They avoid embedding credentials or customer-specific data.

Distribution is through GitHub plus the `skills` CLI:

```bash
npx skills add intelligems-io/intelligems-mcp-skills --list
```

Vercel MCP deployment docs are useful for teams building MCP servers. They are not required for this package because Intelligems already hosts the MCP server.
