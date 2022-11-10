from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .lights.routes import router as light_router

app = FastAPI()

app.include_router(light_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "HELLO WORLD!"
