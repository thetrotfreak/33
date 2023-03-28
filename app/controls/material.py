from flet import AlertDialog
from flet import colors
from flet import Column
from flet import Dropdown
from flet import dropdown
from flet import InputBorder
from flet import Page
from flet import Ref
from flet import Text
from flet import TextStyle
from flet import TextThemeStyle
from flet import UserControl

from utils import Preference


class MaterialYouCustomizationDialog(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pref = Preference(page)
        self.page = page
        self.dropdown = Ref[Dropdown]()
        self.COLORS = sorted(
            [
                "RED",
                "PINK",
                "PURPLE",
                "INDIGO",
                "BLUE",
                "CYAN",
                "TEAL",
                "GREEN",
                "LIME",
                "YELLOW",
                "AMBER",
                "ORANGE",
                "BROWN",
            ]
        )
        self.dialog = AlertDialog(
            title=Text(
                value="Material accent",
                font_family="sans",
                style=TextThemeStyle.TITLE_LARGE,
            ),
            content=Column(
                controls=[
                    Dropdown(
                        ref=self.dropdown,
                        options=[
                            *map(
                                lambda color: dropdown.Option(key=color),
                                self.COLORS,
                            )
                        ],
                        text_style=TextStyle(
                            font_family="sans", color=colors.SECONDARY
                        ),
                        dense=True,
                        filled=True,
                        border=InputBorder.NONE,
                        on_change=lambda event: self._theme(),
                    )
                ],
                tight=True
            ),
        )

    def _theme(self):
        self.pref.update(k="accent", v=self.dropdown.current.value.lower())

    def open(self):
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def build(self):
        return self.dialog
