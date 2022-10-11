import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "HELLO WORLD!"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
