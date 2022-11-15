from http.client import HTTPException
from adafruit_blinka.microcontroller.generic_micropython import Pin
from neopixel import GRB, NeoPixel
from pydantic import BaseModel
from typing import Tuple, List, Literal
import time
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from PIL import Image, ImageDraw, ImageFont
from adafruit_led_animation.color import RED, GREEN, BLUE


LIGHT_TYPES = Literal["square_light", "rectangle_light"]
RAINBOW_TYPES = Literal["cycle", "chase", "comet", "sparkle"]


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
    speed: float


class ColorCyclePostModel(BaseModel):
    light_type = LIGHT_TYPES
    colors = List[Color]
    speed: float


class Light:
    neopixel: NeoPixel
    num_pixels: int
    height_pixels: int
    width_pixels: int

    def __init__(self, pin_id: int, height_pixels: int, width_pixels: int):
        num_pixels = height_pixels * width_pixels

        self.neopixel = NeoPixel(
            Pin(pin_id), num_pixels, brightness=0.01, auto_write=False, pixel_order=GRB
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

    def rainbow_cycle(self, model: RainbowPostModel):
        animation = None

        match model.rainbow_type:
            case "cycle":
                animation = Rainbow(self.neopixel, speed=model.speed)
            case "chase":
                animation = RainbowChase(self.neopixel, speed=model.speed, step=1)
            case "comet":
                animation = RainbowComet(self.neopixel, speed=model.speed)
            case "sparkle":
                animation = RainbowSparkle(self.neopixel, speed=model.speed)
            case _:
                raise HTTPException(
                    status_code=404, detail="Could not find suitable light"
                )

        if animation is not None:
            while True:
                animation.animate()

        def scrolling_text(
            self, cycles: int, text: str, text_speed: float, text_color: Color
        ):
            font = ImageFont.truetype("Quicksand-Regular.ttf", 8)

            # Measure the size of our text
            text_width, text_height = font.getsize(text)
            # Create a new PIL image big enough to fit the text
            image = Image.new(
                "P",
                (
                    text_width + self.width_pixels + self.width_pixels,
                    self.height_pixels,
                ),
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

    def color_cycle(self, colors: List[Color], speed):
        colorcycle = ColorCycle(self.neopixel, colors=[RED, GREEN, BLUE], speed=0.4)
        while True:
            colorcycle.animate()
