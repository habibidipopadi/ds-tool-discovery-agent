import httpx
from typing import Iterable

from ..config import GITHUB_TOKEN
from ..models import Tool


BASE_URL = "https://api.github.com"


async def search_github_tools(query: str, per_page: int = 20) -> Iterable[Tool]:
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    async with httpx.AsyncClient(timeout=20) as client:
        resp = await client.get(
            f"{BASE_URL}/search/repositories",
            params={
                "q": query,
                "sort": "stars",
                "order": "desc",
                "per_page": per_page,
            },
            headers=headers,
        )
        resp.raise_for_status()
        data = resp.json()

    for item in data.get("items", []):
        yield Tool(
            name=item["full_name"],
            source="github",
            url=item["html_url"],
            description=item.get("description") or "",
            tags=item.get("topics", []),
        )
