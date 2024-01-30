from flet import CircleBorder
from flet import Column
from flet import CrossAxisAlignment
from flet import FloatingActionButton
from flet import IconButton
from flet import icons
from flet import KeyboardEvent
from flet import MainAxisAlignment
from flet import Page
from flet import Ref
from flet import Row
from flet import UserControl

from .control import ScrambleControl
from .control import TimerControl


class TimerView(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.expand = True
        self.page = page
        self.route = "/timer"
        self.scramble = ScrambleControl()
        self.timer = TimerControl()
        self.scramble_hook = Ref[IconButton]()
        self.timer_hook = Ref[FloatingActionButton]()
        # if self.page.route == self.route:
        self.page.on_keyboard_event = self.fire

    def fire(self, e: KeyboardEvent):
        if not e.shift and not e.ctrl and not e.alt:
            if e.key.casefold() == "p".casefold():
                self.timer.signal(ref=self.timer_hook)
            elif e.key == "S":
                self.scramble.scramble()
            elif e.key == "X":
                self.page.window_destroy()
            elif e.key == "F":
                if self.page.window_full_screen:
                    self.page.window_full_screen = False
                else:
                    self.page.window_full_screen = True
                self.page.update()

    def build(self):
        return Column(
            expand=True,
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                self.scramble,
                self.timer,
                Row(
                    controls=[
                        IconButton(
                            ref=self.scramble_hook,
                            icon=icons.SHUFFLE,
                            tooltip="Shuffle",
                            on_click=lambda event: self.scramble.scramble(),
                        ),
                        FloatingActionButton(
                            ref=self.timer_hook,
                            icon=icons.PLAY_ARROW,
                            tooltip="Toggle timer",
                            shape=CircleBorder(),
                            on_click=lambda event: self.timer.signal(
                                ref=self.timer_hook
                            ),
                        ),
                        IconButton(
                            icon=icons.HISTORY,
                            tooltip="Reset timer",
                            on_click=lambda event: self.timer.reset(),
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                ),
            ],
        )
