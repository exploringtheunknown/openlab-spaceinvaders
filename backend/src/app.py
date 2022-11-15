from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .lights.routes import router as light_router

description = """
QueensLab OpenLab, fastAPI for creating light animations 🚀

## Lights

You can post different **light** animations, pre-made light effects, or create your own.

## Redis

You will be able to:

* **Get score** (_not implemented_).
* **Save score** (_not implemented_).
"""


app = FastAPI(
    title="QueensLab OpenLab: Space Invaders",
    description=description,
    version="0.0.1",
    docs_url="/",
)

app.include_router(light_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
