from .models.base_light import BaseLight


def getLight() -> BaseLight:
    i = 10

    if i == 10:

        return BaseLight()
    else:
        from .models.light import Light

        return Light(pin_id=21, width_pixels=32, height_pixels=8)
