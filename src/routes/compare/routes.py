import logging

from fastapi import APIRouter

from src.controllers import CompareController
from src.schemas.compare_dto import (
    CompareRequestDto,
    CompareResponseDto,
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/compare", tags=["Compare"])


@router.post("/")
def compare(params: CompareRequestDto) -> CompareResponseDto:
    controller = CompareController()
    result = controller.send(params)
    return result
