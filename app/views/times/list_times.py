from flet import Page
from flet import Text
from flet import TextThemeStyle
from flet import UserControl
from flet import View


class ListTimesView(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.route = "/list_times"
        self.view = View(
            route=self.route,
            controls=[
                self.page.window,
                self.page.navigation_bar,
                Text(
                    value="Listing times...",
                    font_family="sans",
                    style=TextThemeStyle.DISPLAY_LARGE
                ),
            ],
        )
        self.page.views.append(self.view)
        self.page.go(self.route)

    def build(self):
        return self.view
