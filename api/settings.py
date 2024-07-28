from __future__ import annotations

import enum
import re
from contextvars import ContextVar

from pydantic import SecretStr
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

CHANNEL_PREFIX = "UC"
PLAYLIST_PREFIX = "UU"


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
    model_config = SettingsConfigDict(toml_file="settings.toml", env_prefix="YOUTUBE_")

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


settings_var: ContextVar[YouTubeSettings] = ContextVar("settings_var")
