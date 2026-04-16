"""MCP server for agents-example."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("agents-example")


@mcp.tool()
def agents_example_hello(name: str = "World") -> str:
    """Greet someone by name.

    Args:
        name: The name to greet.

    Returns:
        A greeting string.
    """
    return f"Hello, {name}! Welcome to agents-example."


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
