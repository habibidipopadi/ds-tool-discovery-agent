from datetime import datetime
from pydantic import BaseModel


class Tool(BaseModel):
    id: int | None = None
    name: str
    source: str  # github | pypi | huggingface | web
    url: str
    description: str | None = None
    category: str | None = None
    tags: list[str] = []
    quality_score: float | None = None
    popularity_score: float | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
