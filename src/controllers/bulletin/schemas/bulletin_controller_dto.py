from src.schemas.worker_dto import WorkerDto, WorkerStatus


class BulletinControllerDto(WorkerDto):
    status: WorkerStatus = WorkerStatus.progress
    request_content: str
