import logging

from fastapi import APIRouter

from src.services.celery.publishers.bulletin_publisher import publish_task

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/bulletin", tags=["Bulletin"])


@router.post("/")
def retrieve(params: dict) -> dict:
    result = publish_task(params)
    return result


@router.get("/status")
def status() -> None:
    pass
