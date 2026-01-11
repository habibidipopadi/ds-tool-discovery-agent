import asyncio

from .sources.github import search_github_tools
from .sources.pypi import search_pypi_tools
from .ranking import rank_tools


async def crawl_all():
    # Simple v1 crawl: GitHub + PyPI
    github_tools = [t async for t in search_github_tools("data science language:python stars:>2000 topic:data-science")]
    pypi_tools = [t async for t in search_pypi_tools("data science")]

    ranked = rank_tools(github_tools + pypi_tools)

    for t in ranked[:20]:
        print(f"{t.quality_score:.2f} - {t.source} - {t.name} - {t.url}")


if __name__ == "__main__":
    asyncio.run(crawl_all())
