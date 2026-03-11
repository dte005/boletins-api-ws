from ast import Compare

from src.environment import env
from src.schemas import CompareRequestDto, CompareResponseDto
from src.schemas.domains import WorkerStatus
from src.services.celery.celery import celery_app


class Publisher:
    queue: str
    task_name: str = "rpa.compare"

    def __init__(self):
        self.queue = env("QUEUE_COMPARE", "")

    def task(self, params: CompareRequestDto) -> CompareResponseDto:

        result = celery_app.send_task(
            self.task_name,
            args=[params.model_dump(mode="json")],
            queue=self.queue,
        )

        return CompareResponseDto(
            id=result.id,
            status=WorkerStatus.progress,
            task_name=self.task_name,
            queue_name=self.queue,
        )
