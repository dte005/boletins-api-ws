from pydantic import BaseModel

from src.schemas.domains import WorkerStatus


class WorkerDto(BaseModel):
    partition_key: str
    row_key: str


class WorkerStatusDto(WorkerDto):
    status: WorkerStatus = WorkerStatus.progress
    request_content: dict


class WorkerErrorDto(WorkerDto):
    status: WorkerStatus = WorkerStatus.failure
    request_content: dict
    stack_trace: str  # error location
    error_content: str
