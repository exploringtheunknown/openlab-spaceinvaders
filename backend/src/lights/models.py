from adafruit_blinka.microcontroller.generic_micropython import Pin
from neopixel import GRB, NeoPixel
from pydantic import BaseModel
from typing import Tuple, List, Literal

LIGHT_TYPES = Literal["squre_light", "rectangle_light"]


class Color:
    r: int
    g: int
    b: int

    def values(self) -> Tuple[int, int, int]:
        return (self.r, self.g, self.b)


class FillPostModel(BaseModel):
    color: Color
    light_type: LIGHT_TYPES


class FillByIndexItem(BaseModel):
    index: int
    color: Color


class FillByIndexPostModel(BaseModel):
    light_type: LIGHT_TYPES
    index_items: List[FillByIndexItem]


class ScrollingTextPostModel(BaseModel):
    light_type: LIGHT_TYPES
    text: str


class RainbowPostModel(BaseModel):
    light_type: LIGHT_TYPES


class Light(BaseModel):
    neopixel: NeoPixel
    num_pixels: int
    height_pixels: int
    width_pixels: int

    def __init__(self, pin_id: int, height_pixels: int, width_pixels: int):
        num_pixels = height_pixels * width_pixels

        self.neopixel = NeoPixel(
            Pin(pin_id), num_pixels, brightness=0.2, auto_write=False, pixel_order=GRB
        )
        self.height_pixels = height_pixels
        self.width_pixels = width_pixels
        self.num_pixels = num_pixels

    def loading(self, color: Color):
        self.neopixel.fill(color.values())
        self.neopixel.show()

    def fill(self, color: Color):
        self.neopixel.fill(color.values())
        self.neopixel.show()

    def fill_by_index(self, items: List[FillByIndexItem]):
        for pixel in range(self.num_pixels):
            existing_pixel = next((item for item in items if item.index == pixel), None)

            if existing_pixel is not None:
                self.neopixel[pixel] = existing_pixel.color.values()
            else:
                self.neopixel[pixel] = (0, 0, 0)

            self.neopixel.show()
