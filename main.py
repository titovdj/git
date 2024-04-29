from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def name():
    return {'Титов Максим 404б'};
