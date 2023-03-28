from random import choices
from random import randint

from flet import colors
from flet import CrossAxisAlignment
from flet import MainAxisAlignment
from flet import Row
from flet import TextAlign
from flet import TextThemeStyle
from flet import UserControl
from overrides import SansText


class Scramble:
    def __init__(self):
        self._current = ""
        self._standard_moves = [
            "F",
            "F'",
            "F2",
            "B",
            "B'",
            "B2",
            "L",
            "L'",
            "L2",
            "R",
            "R'",
            "R2",
            "U",
            "U'",
            "U2",
            "D",
            "D'",
            "D2",
        ]

    def _generate_scramble(self):
        """
        Return a shuffle as a str
        """
        # TODO: requires a better shuffling algorithm
        # Currently, it can generate shuffles where adjacent moves
        # can cancel out each other i.e., have no effect on the cube's state
        # for example, F B F' or R R'
        return "    ".join(
            choices(
                population=self._standard_moves,
                k=randint(
                    len(self._standard_moves), len(self._standard_moves) + 3
                ),
            )
        )

    @property
    def get(self):
        self._current = self._generate_scramble()
        return self._current


class ScrambleControl(UserControl):
    def __init__(self):
        super().__init__()
        self._control = SansText(
            value=Scramble().get,
            text_align=TextAlign.CENTER,
            style=TextThemeStyle.TITLE_LARGE,
            color=colors.SECONDARY,
        )

    def scramble(self):
        self._control.value = Scramble().get
        self._control.update()

    def build(self):
        return Row(
            expand=1,
            controls=[self._control],
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.CENTER,
        )
