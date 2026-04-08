from typing import Optional

from pydantic import BaseModel

from src.schemas.domains import PipelineType, WorkerStatus


class CompareRequestDto(BaseModel):
    task_id: Optional[str] = None
    bidding_id: str
    type: Optional[PipelineType] = PipelineType.COMPARE


class CompareResponseDto(BaseModel):
    id: str
    status: WorkerStatus
    queue_name: str
    task_name: str
