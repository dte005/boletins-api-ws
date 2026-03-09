import logging
from collections.abc import Mapping
from typing import Any

from fastapi import APIRouter

from src.services.celery.publishers.bidding_compare_publisher import publish_task

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/bidding", tags=["Bidding"])


@router.post("/info")
def retrieve(params: dict) -> dict:
    result = publish_task(params)
    return result


@router.post("/compare")
def compare() -> Mapping[str, Any]:
    return {"message": "done"}
