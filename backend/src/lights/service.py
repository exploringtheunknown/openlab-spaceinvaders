from fastapi import HTTPException
from .models import Light, LIGHT_TYPES


def getLight(light_string: LIGHT_TYPES) -> Light:
    match light_string:
        case "square_light":
            return Light(pin_id=21, width_pixels=16, height_pixels=16)
        case "rectangular_light":
            return Light(pin_id=18, width_pixels=32, height_pixels=8)
        case _:
            raise HTTPException(status_code=404, detail="Could not find suitable light")
