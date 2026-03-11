import logging

from fastapi import APIRouter

from ...controllers import BiddingController
from ...schemas.bidding_dto import BiddingRequestDto, BiddingResponseDto

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/bidding", tags=["Bidding"])


@router.post("/")
def retrieve(params: BiddingRequestDto) -> BiddingResponseDto:
    result = BiddingController().send(params)
    return result
