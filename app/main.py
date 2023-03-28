from flet import app
from flet import padding
from flet import Page

from controls import navigation_bar
from controls import WindowControl
from utils import Preference
from views import TimerView


def main(page: Page):
    Preference(page).load()
    page.title = "33"
    page.fonts = {
        "sans": "fonts/RobotoFlex-Regular.ttf",
        "mono": "fonts/RobotoMono-Bold.ttf",
    }
    page.padding = padding.all(8)
    page.window_min_width = 960
    page.window_min_height = 540
    page.window_title_bar_hidden = True
    page.navigation_bar = navigation_bar(page=page)
    page.add(WindowControl(page=page))
    page.add(TimerView(page=page))
    page.update()


if __name__ == "__main__":
    app(target=main, assets_dir="assets")
