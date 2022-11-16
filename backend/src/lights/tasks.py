from fastpi import BackgroundTask


def animation_task(animation):
    while True:
        animation.animate()


def create_light_task(animation, background_task: BackgroundTask):
    if animation is not None:
        background_task.add_task(animation_task, animation)
