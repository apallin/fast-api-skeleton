from fastapi import APIRouter

from app.logger import get_logger

router = APIRouter()
logger = get_logger(__name__)


@router.get("/hello-world")
async def hello_world() -> str:
    logger.info("Calling hello world")
    return "Hello World"
