from __future__ import annotations

from contextlib import suppress
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, BeforeValidator

from api.dependencies import YouTubeStats, Category, get_stats
from api.settings import YouTubeSettings, settings_var

app = FastAPI()
settings = YouTubeSettings()  # type: ignore[call-arg]

settings_var.set(settings)


class BaseResponse(BaseModel):
    success: bool = True


class StatsReponse(BaseResponse):
    number: int


class AllStatsReponse(BaseResponse):
    stats: YouTubeStats


def category_from_name(name: str | int) -> Category | None:
    with suppress(ValueError):
        name = int(name)
    if isinstance(name, str):
        return Category._member_map_.get(name)  # type: ignore[return-value]
    return Category(name)


@app.get("/stats/{category}")
async def stats(
    category: Annotated[Category | None, BeforeValidator(category_from_name)],
    stats: Annotated[YouTubeStats, Depends(get_stats)],
) -> StatsReponse:
    if category is None or category not in stats:
        raise HTTPException(
            status_code=404,
            detail=f"available categories are: {', '.join(Category._member_names_)}",
        )
    return StatsReponse(number=stats[category])


@app.get("/stats")
async def all_stats(
    stats: Annotated[YouTubeStats, Depends(get_stats)],
) -> AllStatsReponse:
    return AllStatsReponse(stats=stats)
