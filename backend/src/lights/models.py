from adafruit_blinka.microcontroller.generic_micropython import Pin
from neopixel import GRB, NeoPixel, Color
from pydantic import BaseModel 
from typing import Tuple, List


class Light(BaseModel):
    neopixel: NeoPixel
    num_pixels: int
    height_pixels: int
    width_pixels: int
 
    def __init__(self, pin_id: int, height_pixels: int, width_pixels: int):
        num_pixels = height_pixels * width_pixels

        self.neopixel = NeoPixel(Pin(pin_id), num_pixels, brightness=0.2, auto_write=False, pixel_order=GRB)
        self.height_pixels = height_pixels
        self.width_pixels = width_pixels
        self.num_pixels = num_pixels
    
    def loading(self, color: Color):
        self.neopixel.fill(color)
        self.neopixel.show()

    def fill(self, color: Tuple[int]):
        self.neopixel.fill(color)
        self.neopixel.show()

    def fill_by_index(self, indexes: List[dict]):
        for pixel in range(self.num_pixels):
            existing_pixel = indexes[0]

            if existing_pixel is not None:
                self.neopixel[pixel] = existing_pixel['color']
            else:
                self.neopixel[pixel] = (0,0,0)

            self.neopixel.show()
