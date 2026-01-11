import httpx
from typing import Iterable

from src.models import Tool
from src.config import PYPI_BASE_URL


async def search_pypi_tools(term: str, limit: int = 20) -> Iterable[Tool]:
    try:
        async with httpx.AsyncClient(timeout=20) as client:
            resp = await client.get("https://pypi.org/search/", params={"q": term, "format": "json"})
            resp.raise_for_status()
            data = resp.json()
    except Exception as e:
        print(f"PyPI search failed: {e}")
        return

    for r in data.get("projects", [])[:limit]:
        name = r["name"]
        yield Tool(
            name=name,
            source="pypi",
            url=f"https://pypi.org/project/{name}/",
            description=r.get("description") or "",
            tags=["pypi"],
        )