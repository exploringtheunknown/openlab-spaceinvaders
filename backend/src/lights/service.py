from fastapi import HTTPException
from .models import Light, LIGHT_TYPES


def getLight(light_type: LIGHT_TYPES) -> Light:
    if light_type == "square_light":
        return Light(pin_id=21, width_pixels=16, height_pixels=16)
    else if "rectangle_light":
        return Light(pin_id=21, width_pixels=32, height_pixels=8)
    else:
        raise HTTPException(status_code=404, detail="Could not find suitable light")
