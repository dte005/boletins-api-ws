import logging

from fastapi import APIRouter

from src.controllers.bulletin.bulletin_controller import BulletinController
from src.errors_handlers import BusinessException
from src.schemas.bulletin_dto import (
    BulletinRequestDto,
    BulletinResponseDto,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/bulletin", tags=["Bulletin"])


@router.post("/")
def retrieve(params: BulletinRequestDto) -> BulletinResponseDto:
    controller = BulletinController()
    result = controller.get_bulletin(params)
    logger.info(f"Bulletin response: {result.model_dump(mode='json')}")
    return result


@router.get("/status")
def status() -> None:
    raise BusinessException(message="business test error tester")
