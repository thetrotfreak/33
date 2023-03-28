from flet import CrossAxisAlignment
from flet import IconButton
from flet import icons
from flet import MainAxisAlignment
from flet import Page
from flet import Row
from flet import UserControl
from flet import WindowDragArea

from .menu import MenuControl


class WindowControl(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

    def build(self):
        return Row(
            controls=[
                WindowDragArea(content=IconButton(icon=icons.DRAG_INDICATOR)),
                MenuControl(page=self.page),
            ],
            expand=True,
            alignment=MainAxisAlignment.END,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )
