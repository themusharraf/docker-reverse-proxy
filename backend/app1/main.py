from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Web server 1": "FastAPI App"}
