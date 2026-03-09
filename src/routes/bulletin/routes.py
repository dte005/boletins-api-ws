import logging

from fastapi import APIRouter

from src.services.celery.publishers.bulletin.bulletin_publisher import publish_task
from src.services.celery.publishers.bulletin.schemas.api_dto import (
    BulletinRequestDto,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/bulletin", tags=["Bulletin"])


@router.post("/")
def retrieve(params: BulletinRequestDto) -> dict:
    result = publish_task(params)
    return result


@router.get("/status")
def status() -> None:
    pass
