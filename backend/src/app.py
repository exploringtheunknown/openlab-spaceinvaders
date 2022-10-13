from fastapi import FastAPI
from .lights.routes import router as light_router

app = FastAPI()

app.include_router(light_router)


@app.get("/")
def root():
    return "HELLO WORLD!"
