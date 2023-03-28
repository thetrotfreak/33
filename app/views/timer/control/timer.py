from threading import Thread
from time import sleep

from flet import colors
from flet import CrossAxisAlignment
from flet import FloatingActionButton
from flet import icons
from flet import MainAxisAlignment
from flet import Page
from flet import Ref
from flet import Row
from flet import TextAlign
from flet import TextThemeStyle
from flet import UserControl
from overrides import MonoText


class TimerControl(UserControl):
    def __init__(self, page: Page = None):
        super().__init__()
        self.page = page
        self._ticking = False
        self._clock = "{:02d}:{:02d}.{:02d}"
        self._timer = MonoText(
            value=self._clock.format(0, 0, 0),
            text_align=TextAlign.CENTER,
            style=TextThemeStyle.DISPLAY_LARGE,
            color=colors.PRIMARY
        )
        self._centi_second = 0

    def signal(self, ref: Ref[FloatingActionButton]):
        """
        Toggles the timer to start or stop.
        """
        if not self._ticking:
            self._ticking = True
            ref.current.icon = icons.PAUSE
            ref.current.update()
            timer_thread = Thread(target=self._update_timer, args=())
            timer_thread.start()
            timer_thread.join()
        else:
            ref.current.icon = icons.PLAY_ARROW
            ref.current.update()
            self._ticking = False

    def _update_timer(self):
        """
        Updates the timer every 100th of a second.
        """
        while self._ticking:
            second, centi_second = divmod(self._centi_second, 100)
            minute, second = divmod(second, 60)
            self._timer.value = self._clock.format(
                minute, second, centi_second
            )
            # self._timer.update()
            self.update()
            sleep(1 / 100)
            self._centi_second += 1

        # reset the timer everytime it is re-started
        self._centi_second = 0

    def build(self):
        return Row(
            controls=[self._timer],
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )
