from fastapi import FastAPI

from app.routers import hello_world

app = FastAPI()

# Include routers from subfolders
app.include_router(hello_world.router)


@app.get("/")
async def root() -> dict:
    return {"message": "Fast API Skeleton"}
