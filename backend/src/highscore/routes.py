from fastapi import APIRouter


router = APIRouter(prefix="/highscore", tags=["Highscore"])


@router.get("/highscore")
async def get_highscore():
    return ""


@router.get("/highscore/{name}")
async def get_highscore_by_name(name: str):
    return ""


@router.post("/highscore")
async def post_highscore():
    return ""


@router.delete("/highscore/{name}")
async def delete_highscore_by_name(name: str):
    return ""
