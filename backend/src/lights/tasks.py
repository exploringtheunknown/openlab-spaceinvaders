import asyncio
from functools import lru_cache

@lru_cache
def getEventLoop():
    return asyncio.new_event_loop()

loop = getEventLoop()
task = None;

def cancel_tasks():
    tasks = [task.cancel() for task in asyncio.all_tasks() if task.get_name() == 'light']
    
async def animation_task(animation):
    while True:
        animation.animate()
        await asyncio.sleep(0.001)

async def create_light_task(animation):
    print('createing task')
    if animation is not None:
        asyncio.create_task(animation_task(animation), name="light")
    