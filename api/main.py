from __future__ import annotations

from typing import Annotated

from fastapi import Depends, FastAPI

from api.dependencies import YouTubeStats, get_stats
from api.settings import YouTubeSettings, settings_var

app = FastAPI()
settings = YouTubeSettings()  # type: ignore[call-arg]

settings_var.set(settings)


@app.get("/stats")
async def stats(stats: Annotated[YouTubeStats, Depends(get_stats)]) -> YouTubeStats:
    return stats
