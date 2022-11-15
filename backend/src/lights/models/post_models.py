from pydantic import BaseModel
from .color import Color
from typing import Literal, List

RAINBOW_TYPES = Literal["cycle", "chase", "comet", "sparkle"]


class FillPostModel(BaseModel):
    color: Color


class FillByIndexItem(BaseModel):
    index: int
    color: Color


class FillByIndexPostModel(BaseModel):
    index_items: List[FillByIndexItem]


class ScrollingTextPostModel(BaseModel):
    text: str
    cycles: int
    text_speed: float
    color: Color


class RainbowPostModel(BaseModel):
    rainbow_type: RAINBOW_TYPES
    speed: float


class ColorCyclePostModel(BaseModel):
    colors: List[Color]
    speed: float
