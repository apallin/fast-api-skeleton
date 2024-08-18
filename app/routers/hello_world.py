from fastapi import APIRouter

router = APIRouter()


@router.get("/hello-world")
async def hello_world() -> str:
    return "Hello World"
