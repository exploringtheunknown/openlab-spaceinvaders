from fastapi import HTTPException, BackgroundTasks
from adafruit_blinka.microcontroller.generic_micropython import Pin
from neopixel import GRB, NeoPixel
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowsparkle import RainbowSparkle
from neopixel import GRB, NeoPixel
from PIL import Image, ImageDraw, ImageFont
from typing import List
import time
from .color import Color
from .base_light import BaseLight
from .post_models import FillByIndexItem, RainbowPostModel
from ..tasks import create_light_task, cancel_tasks


class Light(BaseLight):
    neopixel: NeoPixel
    num_pixels: int
    height_pixels: int
    width_pixels: int
    background_tasks: BackgroundTasks

    def __init__(self, pin_id: int, height_pixels: int, width_pixels: int, background_tasks: BackgroundTasks):
        cancel_tasks()
        num_pixels = height_pixels * width_pixels

        self.neopixel = NeoPixel(
            Pin(pin_id), num_pixels, brightness=0.01, auto_write=False, pixel_order=GRB
        )
        self.height_pixels = height_pixels
        self.width_pixels = width_pixels
        self.num_pixels = num_pixels
        self.background_tasks = background_tasks

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

    async def rainbow_cycle(self, model: RainbowPostModel):
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

        await create_light_task(animation)

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
        animation = ColorCycle(self.neopixel, colors=colors, speed=speed)
        create_light_task(animation)
    
    def create_task(self, animation):
        if animation is not None:
            while True:
                animation.animate()
