from fastapi import APIRouter
from .service import getLight
from .models import (
    FillPostModel,
    FillByIndexPostModel,
    ScrollingTextPostModel,
    RainbowPostModel,
)


router = APIRouter(prefix="/lights", tags=["lights"])


@router.post("/")
async def post_light_loading():
    return [{""}]


@router.post("/fill")
async def post_light_fill(model: FillPostModel):
    light = getLight(model.light_type)
    light.fill(model.color)
    return f"Started light {model.light_type} with color {model.color}"


@router.post("/fill_by_index")
async def post_light_fill_by_index(model: FillByIndexPostModel):
    light = getLight(model.light_type)
    light.fill_by_index(model.index_items)
    return f"Started light {model.light_type} with color {model.color}"


@router.post("/scrolling_text")
async def post_light_scrolling_text(model: ScrollingTextPostModel):
    light = getLight(model.light_type)
    light.scrolling_text(model.cycles, model.text, model.text_speed, model.color)
    return [{""}]


@router.post("/rainbow")
async def post_light_rainbow(model: RainbowPostModel):
    light = getLight(model.light_type)
    light.rainbow_cycle(model.cycles)
    return [{""}]
