from fastmcp import FastMCPServer, Tool

from ..ranking import rank_tools
from ..sources.github import search_github_tools
from ..sources.pypi import search_pypi_tools


server = FastMCPServer("ds-tool-discovery-agent")


@server.tool()
async def search_tools(query: str) -> list[dict]:
    """Search for data science tools matching the query across GitHub and PyPI, returning ranked results."""
    github_tools = [t async for t in search_github_tools(query)]
    pypi_tools = [t async for t in search_pypi_tools(query)]
    ranked = rank_tools(github_tools + pypi_tools)[:20]
    return [t.model_dump() for t in ranked]


if __name__ == "__main__":
    server.run()
