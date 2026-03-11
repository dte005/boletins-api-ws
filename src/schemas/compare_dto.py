from typing import Optional

from pydantic import BaseModel

from src.schemas.domains import PipelineType, WorkerStatus


class CompareRequestDto(BaseModel):
    type: Optional[PipelineType] = PipelineType.COMPARE


class CompareResponseDto(BaseModel):
    id: str
    status: WorkerStatus
    queue_name: str
    task_name: str
