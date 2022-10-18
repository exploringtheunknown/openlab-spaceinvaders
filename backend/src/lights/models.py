from adafruit_blinka.microcontroller.generic_micropython import Pin
from neopixel import GRB, NeoPixel
from pydantic import BaseModel
from typing import Tuple, List, Literal
import time
from PIL import Image, ImageDraw, ImageFont


LIGHT_TYPES = Literal["square_light", "rectangle_light"]


class Color(BaseModel):
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
    cycles: int
    text_speed: float
    color: Color


class RainbowPostModel(BaseModel):
    light_type: LIGHT_TYPES
    cycles: int


class Light:
    neopixel: NeoPixel
    num_pixels: int
    height_pixels: int
    width_pixels: int

    def __init__(self, pin_id: int, height_pixels: int, width_pixels: int):
        num_pixels = height_pixels * width_pixels

        self.neopixel = NeoPixel(
            Pin(pin_id), num_pixels, brightness=0.1, auto_write=False, pixel_order=GRB
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

    @staticmethod
    def wheel(pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos * 3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos * 3)
            g = 0
            b = int(pos * 3)
        else:
            pos -= 170
            r = 0
            g = int(pos * 3)
            b = int(255 - pos * 3)
        return (r, g, b)

    def rainbow_cycle(self, cycles: int):
        for c in range(cycles):
            for j in range(255):
                for i in range(self.num_pixels):
                    pixel_index = (i * 256 // self.num_pixels) + j
                    self.neopixel[i] = self.wheel(pixel_index & 255)
                self.neopixel.show()
                time.sleep(0.001)

    def scrolling_text(
        self, cycles: int, text: str, text_speed: float, text_color: Color
    ):
        font = ImageFont.truetype("Quicksand-Regular.ttf", 8)

        # Measure the size of our text
        text_width, text_height = font.getsize(text)

        # Create a new PIL image big enough to fit the text
        image = Image.new(
            "P",
            (text_width + self.width_pixels + self.width_pixels, self.height_pixels),
            0,
        )
        draw = ImageDraw.Draw(image)

        draw.text((self.width_pixels, -1), text, font=font, fill=255)
        image.save("img.png", "PNG")
        offset_x = 0

        for c in range(cycles):
            for x in range(self.width_pixels):
                for y in range(self.height_pixels):
                    if image.getpixel((x + offset_x, y)) == 255:
                        self.neopixel[self.getIndex(x, y)] = text_color.values()

                    else:
                        self.neopixel[self.getIndex(x, y)] = (0, 0, 0)

            offset_x += 1
            if offset_x + self.width_pixels > image.size[0]:
                offset_x = 0

            self.neopixel.show()
            time.sleep(text_speed)  # scrolling text speed

    def getIndex(self, x, y):
        x = self.width_pixels - x - 1
        if x % 2 != 0:
            return (x * 8) + y
        else:
            return (x * 8) + (7 - y)
