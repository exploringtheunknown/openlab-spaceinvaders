from .models.base_light import BaseLight
import os
from fastapi import BackgroundTasks


def getLight(background_tasks: BackgroundTasks) -> BaseLight:
    user = os.environ.get("SUDO_USER")
    print(user)
    if user == "pi":
        from .models.light import Light

        return Light(pin_id=21, width_pixels=32, height_pixels=8, background_tasks=background_tasks)
    else:
        return BaseLight()
