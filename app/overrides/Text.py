from flet import Text


class SansText(Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_family = "sans"


class MonoText(Text):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font_family = "mono"
