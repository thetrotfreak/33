from flet import Divider
from flet import Icon
from flet import icons
from flet import Page
from flet import PopupMenuButton
from flet import PopupMenuItem
from flet import Row
from flet import UserControl
from overrides import SansText

from .material import MaterialYouCustomizationDialog
from .theme import ChooseThemeDialog


class MenuControl(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def build(self):
        return PopupMenuButton(
            items=[
                PopupMenuItem(
                    # icon=icons.KEYBOARD,
                    # text="keyboard shortcuts".title()
                    content=Row(
                        expand=1,
                        controls=[
                            Icon(name=icons.KEYBOARD),
                            SansText("Keyboard Shortcuts")
                        ]
                    )
                ),
                Divider(),
                PopupMenuItem(
                    icon=icons.BRIGHTNESS_4,
                    text="app theme".title(),
                    on_click=lambda event: ChooseThemeDialog(
                        page=self.page
                    ).open(),
                ),
                PopupMenuItem(
                    icon=icons.COLOR_LENS,
                    text="accent color".title(),
                    on_click=lambda event: MaterialYouCustomizationDialog(
                        page=self.page
                    ).open(),
                ),
                Divider(),
                PopupMenuItem(
                    icon=icons.EXIT_TO_APP,
                    text="Exit",
                    on_click=lambda event: self.page.window_destroy(),
                ),
            ]
        )
