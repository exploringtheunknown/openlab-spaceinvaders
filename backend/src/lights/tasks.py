import asyncio


def cancel_light_tasks():
    for task in asyncio.all_tasks():
        task.cancel()


def animation_task(animation):
    while True:
        animation.animate()


def create_light_task(animation):
    asyncio.create_task(animation_task(animation))
