from typing import Optional

from pydantic import BaseModel

from src.schemas.domains import PipelineType, WorkerStatus


class BiddingRequestDto(BaseModel):
    task_id: Optional[str] = None
    bidding_id: str
    type: Optional[PipelineType] = PipelineType.BIDDING


class BiddingResponseDto(BaseModel):
    id: str
    status: WorkerStatus
    queue_name: str
    task_name: str
