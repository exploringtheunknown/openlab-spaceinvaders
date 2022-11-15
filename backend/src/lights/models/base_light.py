from typing import List
from .color import Color

from .post_models import FillByIndexItem, RainbowPostModel

# base light class exists to be able to debug the project on win/mac/linux
class BaseLight:
    def loading(self, color: Color):
        pass

    def fill(self, color: Color):
        pass

    def fill_by_index(self, items: List[FillByIndexItem]):
        pass

    def rainbow_cycle(self, model: RainbowPostModel):
        pass

    def scrolling_text(
        self, cycles: int, text: str, text_speed: float, text_color: Color
    ):
        pass

    def color_cycle(self, colors: List[Color], speed):
        pass
