from json import dump
from json import JSONDecodeError
from json import load
from pathlib import Path
from typing import NamedTuple

from flet_core import colors
from flet_core import Page
from flet_core import Theme
from flet_core import ThemeMode
from jsonschema import validate
from jsonschema import ValidationError


class Configuration(NamedTuple):
    path: Path
    schema: dict
    default: dict


class Preference:
    __config__ = Configuration(
        path=Path(__file__).parent.parent.joinpath("data", "config.json"),
        schema={
            "type": "object",
            "properties": {
                "theme": {"type": "string", "minLength": 4, "maxLength": 6},
                "accent": {"type": "string", "minLength": 3},
            },
        },
        default={"theme": ThemeMode.SYSTEM.value, "accent": colors.BLUE}
    )
    config = {"theme": ThemeMode.SYSTEM.value, "accent": colors.BLUE}

    def __init__(self, page: Page):
        self.page = page

    @staticmethod
    def _config_follows_schema(config: dict):
        """
        Validate config.json on disk; ill-formatted JSON will result in the
        config.json being overwritten with the default configuration.
        """
        try:
            validate(instance=config, schema=Preference.__config__.schema)
        except ValidationError:
            return False
        else:
            return True

    def load(self):
        """
        Load config.json from disk if found; otherwise load the default
        configuration and save it to disk.
        """
        if not Preference.__config__.path.exists():
            Preference.__config__.path.parent.mkdir()
            Preference.__config__.path.touch()
            self._save()
        else:
            with open(Preference.__config__.path, "r") as f:
                try:
                    config = load(f)
                except JSONDecodeError:
                    # thrown when config.json is present on disk, but is
                    # empty
                    self._save()
                else:
                    if Preference._config_follows_schema(config):
                        self._load_helper(config)
                    else:
                        self._save()

    def _load_helper(self, config):
        Preference.config.update(config)
        self.page.theme_mode = config.get("theme")
        self.page.theme = Theme(color_scheme_seed=config.get("accent"))
        self.page.dark_theme = Theme(color_scheme_seed=config.get("accent"))
        self.page.update()

    def update(self, k, v):
        """
        Call this to persist changes by writing it to config.json
        Also updates the page
        """
        Preference.config.update({k: v})
        Preference._save()
        self.load()

    @staticmethod
    def _save():
        with open(Preference.__config__.path, "w") as f:
            dump(obj=Preference.config, fp=f)
