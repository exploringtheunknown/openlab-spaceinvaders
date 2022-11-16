from fastapi import APIRouter, BackgroundTasks
from .service import getLight
from .models.post_models import (
    ColorCyclePostModel,
    FillPostModel,
    FillByIndexPostModel,
    ScrollingTextPostModel,
    RainbowPostModel,
)


router = APIRouter(prefix="/lights", tags=["Lights"])


@router.post("/")
async def post_light_loading():
    return [{""}]


@router.post("/fill")
async def post_light_fill(model: FillPostModel, background_tasks: BackgroundTasks):
    light = getLight(background_tasks)
    light.fill(model.color)
    return f"Started light with color {model.color}"


@router.post("/fill_by_index")
async def post_light_fill_by_index(model: FillByIndexPostModel, background_tasks: BackgroundTasks):
    light = getLight(background_tasks)
    light.fill_by_index(model.index_items)
    return [{""}]


@router.post("/scrolling_text")
async def post_light_scrolling_text(model: ScrollingTextPostModel, background_tasks: BackgroundTasks):
    light = getLight(background_tasks)
    light.scrolling_text(model.cycles, model.text, model.text_speed, model.color)
    return [{""}]


@router.post("/rainbow")
async def post_light_rainbow(model: RainbowPostModel, background_tasks: BackgroundTasks):
    light = getLight(background_tasks)
    await light.rainbow_cycle(model)
    return [{""}]


@router.post("/color_cycle")
async def post_color_cycle(model: ColorCyclePostModel, background_tasks: BackgroundTasks):
    light = getLight(background_tasks)
    light.color_cycle(colors=model.colors, speed=model.speed)
