from flet import AlertDialog
from flet import Column
from flet import ControlEvent
from flet import CrossAxisAlignment
from flet import MainAxisAlignment
from flet import Page
from flet import Radio
from flet import RadioGroup
from flet import Text
from flet import TextThemeStyle
from flet import ThemeMode
from flet import UserControl

from utils import Preference


class ChooseThemeDialog(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pref = Preference(page)
        self.page = page
        self.dialog = AlertDialog(
            title=Text(
                value="Choose theme",
                font_family="sans",
                style=TextThemeStyle.TITLE_LARGE,
            ),
            content=Column(
                controls=[
                    RadioGroup(
                        content=Column(
                            controls=[
                                *map(
                                    lambda enum: Radio(
                                        value=enum[1].value, label=enum[1].value.title()
                                    ),
                                    ThemeMode._member_map_.items(),
                                )
                            ]
                        ),
                        on_change=self._theme_mode,
                    )
                ],
                alignment=MainAxisAlignment.START,
                horizontal_alignment=CrossAxisAlignment.START,
                tight=True,
            ),
        )

    def _theme_mode(self, event: ControlEvent):
        self.pref.update(k="theme", v=event.control.value)

    def open(self):
        self.page.dialog = self.dialog
        self.dialog.open = True
        self.page.update()

    def build(self):
        return self.dialog
