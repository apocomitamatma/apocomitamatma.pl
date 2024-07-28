from __future__ import annotations

from collections import Counter
from typing import TYPE_CHECKING, Annotated, Literal

from aiocache import cached  # type: ignore[import-untyped]
from httpx import AsyncClient, QueryParams
from pydantic import AliasGenerator, BaseModel, ConfigDict, Field, TypeAdapter
from pydantic.alias_generators import to_camel

from app.settings import Category, settings_var

if TYPE_CHECKING:
    from typing import TypeAlias


class YouTubeVideo(BaseModel):
    id: str
    categories: Category


YouTubeStats: TypeAlias = dict[Category, Annotated[int, Field(default=0)]]


class YouTubePlaylistItemSnippet(BaseModel):
    description: str


class YouTubePlaylistItemResource(BaseModel):
    kind: Literal["youtube#playlistItem"]
    etag: str
    id: str
    snippet: YouTubePlaylistItemSnippet


class YouTubePlaylistItemListResponse(BaseModel):
    kind: Literal["youtube#playlistItemListResponse"]
    etag: str
    next_page_token: str | None = None
    items: list[YouTubePlaylistItemResource] = Field(default_factory=list)

    model_config = ConfigDict(alias_generator=AliasGenerator(validation_alias=to_camel))


class YouTubeRequest(BaseModel):
    key: str
    part: str = "snippet"

    model_config = ConfigDict(
        alias_generator=AliasGenerator(serialization_alias=to_camel),
    )


class YouTubeListRequest(YouTubeRequest):
    playlist_id: str
    max_results: int = 50
    page_token: str | None = None


def get_categories_from_description(description: str) -> Category:
    settings = settings_var.get()
    flags = Category(0)
    for category, pattern in settings.category_patterns.items():
        if category.is_bulk and flags:
            break
        if pattern.findall(description):
            flags |= category
    return flags


async def fetch_videos(
    page_token: str | None = None,
) -> tuple[list[YouTubeVideo], str | None]:
    settings = settings_var.get()
    params = YouTubeListRequest(
        key=settings.api_key.get_secret_value(),
        playlist_id=settings.playlist_id,
        page_token=page_token,
    )

    async with AsyncClient() as client:
        raw = await client.get(
            settings.playlists_endpoint,
            params=QueryParams(**params.model_dump(exclude_none=True)),
        )
        response = YouTubePlaylistItemListResponse(**raw.json())
        videos = [
            YouTubeVideo(
                id=item.id,
                categories=get_categories_from_description(
                    item.snippet.description,
                ),
            )
            for item in response.items
        ]

    return videos, response.next_page_token


@cached(ttl=24 * 60 * 60)
async def fetch_all_videos() -> list[YouTubeVideo]:
    """Fetch all videos from the configured playlist. Exhausts all pages."""
    videos, next_page = await fetch_videos()
    while next_page:
        new_videos, next_page = await fetch_videos(next_page)
        videos.extend(new_videos)
    return TypeAdapter(list[YouTubeVideo]).validate_python(videos)


async def get_stats() -> YouTubeStats:
    videos = await fetch_all_videos()
    counter: YouTubeStats = Counter()
    for video in videos:
        counter.update(video.categories)  # type: ignore[arg-type]
    return counter
