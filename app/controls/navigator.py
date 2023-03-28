from flet import ControlEvent
from flet import icons
from flet import NavigationBar
from flet import NavigationDestination
from flet import Page


def navigation_bar_change(event: ControlEvent, page: Page):
    pass
    # if page.navigation_bar.selected_index == 0:
    #     view = TimerView(page=page)
    #     page.views.clear()
    #     page.views.append(view)
    #     page.route = view.route
    # elif page.navigation_bar.selected_index == 1:
    #     view = ListTimesView(page=page)
    #     page.views.clear()
    #     page.views.append(view)
    #     page.route = view.route


def navigation_bar(page: Page):
    """
    Returns a NavigationBar control
    """
    return NavigationBar(
        destinations=[
            NavigationDestination(
                icon=icons.TIMER_OUTLINED,
                selected_icon=icons.TIMER,
                label="Timer",
            ),
            NavigationDestination(
                icon=icons.VIEW_LIST_OUTLINED,
                selected_icon=icons.VIEW_LIST,
                label="List Times",
            ),
        ],
        on_change=lambda event: navigation_bar_change(event, page=page),
        selected_index=0
    )
