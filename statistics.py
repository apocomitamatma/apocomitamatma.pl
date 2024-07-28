from __future__ import annotations

import asyncio
import enum
import re
from collections import Counter
from contextvars import ContextVar
from pathlib import Path
from typing import TYPE_CHECKING, Annotated, Literal

import typer
from httpx import AsyncClient, QueryParams
from pydantic import (
    AliasGenerator,
    BaseModel,
    ConfigDict,
    Field,
    TypeAdapter,
    SecretStr,
)
from pydantic.alias_generators import to_camel
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

if TYPE_CHECKING:
    from typing import TypeAlias

CHANNEL_PREFIX = "UC"
PLAYLIST_PREFIX = "UU"

settings_var: ContextVar[YouTubeSettings] = ContextVar("settings_var")


class Category(enum.IntFlag, boundary=enum.FlagBoundary.CONFORM):
    e8 = 1 << 0
    mp = 1 << 1
    mr = 1 << 2
    m = mp | mr

    @property
    def is_bulk(self) -> bool:
        return self is self.m


class YouTubeSettings(BaseSettings):
    channel_id: str
    api_key: SecretStr
    playlists_endpoint: str = "https://www.googleapis.com/youtube/v3/playlistItems"
    category_patterns: dict[Category, re.Pattern]
    model_config = SettingsConfigDict(
        toml_file="statistics.toml",
        env_prefix="YOUTUBE_",
        env_file=".env",
    )

    @property
    def playlist_id(self) -> str:
        playlist_id = self.channel_id
        if playlist_id.startswith(CHANNEL_PREFIX):
            id_part = playlist_id.removeprefix(CHANNEL_PREFIX)
            playlist_id = PLAYLIST_PREFIX + id_part
        return playlist_id

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            TomlConfigSettingsSource(settings_cls),
            env_settings,
            dotenv_settings,
            file_secret_settings,
        )


class YouTubeVideo(BaseModel):
    id: str
    categories: Category


YouTubeStatistics: TypeAlias = dict[str, Annotated[int, Field(default=0)]]


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


async def fetch_all_videos() -> list[YouTubeVideo]:
    """Fetch all videos from the configured playlist. Exhausts all pages."""
    videos, next_page = await fetch_videos()
    while next_page:
        new_videos, next_page = await fetch_videos(next_page)
        videos.extend(new_videos)
    return TypeAdapter(list[YouTubeVideo]).validate_python(videos)


async def get_stats() -> YouTubeStatistics:
    videos = await fetch_all_videos()
    counter: dict[Category, int] = Counter()
    for video in videos:
        counter.update(video.categories)  # type: ignore[arg-type]
    return {
        category.name: count for category, count in counter.items() if category.name
    }


class Statistics(BaseModel):
    video_count: YouTubeStatistics

    model_config = ConfigDict(
        alias_generator=AliasGenerator(serialization_alias=to_camel)
    )


cli = typer.Typer()


@cli.command()
def main(
    # settings_file: str = "statistics.toml",
    out_file: Path = Path("front/src/lib/statistics.json"),
) -> None:
    settings = YouTubeSettings()  # type: ignore[call-arg]
    settings_var.set(settings)
    video_count = asyncio.run(get_stats())
    statistics = Statistics(video_count=video_count)
    out_file.write_text(statistics.model_dump_json(by_alias=True))


if __name__ == "__main__":
    cli()