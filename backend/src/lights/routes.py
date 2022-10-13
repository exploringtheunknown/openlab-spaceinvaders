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
    light.fill_by_index(model.color, {**model.index_list})
    return f"Started light {model.light_type} with color {model.color}"


@router.post("/scrolling_text")
async def post_light_scrolling_text(model: ScrollingTextPostModel):
    return [{""}]


@router.post("/rainbow")
async def post_light_rainbow(model: RainbowPostModel):
    return [{""}]
