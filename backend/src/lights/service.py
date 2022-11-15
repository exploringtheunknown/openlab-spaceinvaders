from .models.base_light import BaseLight
import os


def getLight() -> BaseLight:
    user = os.environ.get("USER")
    print(user)
    if user == "pi":
        from .models.light import Light

        return Light(pin_id=21, width_pixels=32, height_pixels=8)
    else:
        return BaseLight()
