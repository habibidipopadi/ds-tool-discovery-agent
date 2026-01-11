from typing import Iterable

from ..models import Tool


def naive_score(tool: Tool) -> Tool:
    """Very simple heuristic scoring placeholder.

    v1: prefer GitHub repos with more topics and longer descriptions.
    """
    desc_len = len((tool.description or "").split())
    tag_bonus = len(tool.tags)
    base = 0.0
    if tool.source == "github":
        base += 0.5
    if tool.source == "pypi":
        base += 0.3

    tool.quality_score = base + min(desc_len / 100.0, 0.5) + min(tag_bonus * 0.05, 0.5)
    return tool


def rank_tools(tools: Iterable[Tool]) -> list[Tool]:
    scored = [naive_score(t) for t in tools]
    return sorted(scored, key=lambda t: t.quality_score or 0, reverse=True)
