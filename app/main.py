from fastapi import FastAPI

from .routers import hello_world

# Create App
app = FastAPI()

# Include routers from subfolders
app.include_router(hello_world.router)


@app.get("/")
async def root():
    return {"message": "Fast API Skeleton"}
