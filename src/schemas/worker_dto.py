from pydantic import BaseModel

from src.schemas.domains import WorkerStatus


class WorkerDto(BaseModel):
    PartitionKey: str
    RowKey: str


class WorkerStatusDto(WorkerDto):
    status: WorkerStatus = WorkerStatus.progress
    request_content: str


class WorkerErrorDto(WorkerDto):
    status: WorkerStatus = WorkerStatus.failure
    request_content: dict
    stack_trace: str  # error location
    error_content: str
