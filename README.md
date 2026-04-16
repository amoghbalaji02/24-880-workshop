# agents-example

Example extension for the 24-880 workshop, installable on both **Claude Code** and **Gemini CLI**.

## Install

### Claude Code (plugin)

Inside a Claude Code session:

```
/plugin marketplace add amoghbalaji02/24-880-workshop
```

```
/plugin install agents-example@agents-example
```

After installing, reload plugins and verify the MCP server is connected with `/reload-plugins` and `/mcp`.

### Gemini CLI (extension)

```bash
gemini extensions install https://github.com/amoghbalaji02/24-880-workshop
```

## Development

### Local setup

```bash
git clone git@github.com:amoghbalaji02/24-880-workshop.git
cd 24-880-workshop
uv sync
```

#### Claude Code

```bash
claude --plugin-dir .
```

#### Gemini CLI

```bash
gemini extensions install .
```

## License

See [LICENSE](LICENSE).