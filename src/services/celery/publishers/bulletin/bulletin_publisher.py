from src.environment import env
from src.schemas.bulletin_dto import BulletinRequestDto, BulletinResponseDto
from src.schemas.domains import WorkerStatus
from src.services.celery.celery import celery_app


class Publisher:
    queue: str
    task_name: str = "rpa.bulletin"

    def __init__(self):
        self.queue = env("QUEUE_BULLETIN", "")

    def task(self, params: BulletinRequestDto) -> BulletinResponseDto:

        result = celery_app.send_task(
            self.task_name,
            args=[params.model_dump(mode="json")],
            queue=self.queue,
        )

        return BulletinResponseDto(
            id=result.id,
            status=WorkerStatus.progress,
            task_name=self.task_name,
            queue_name=self.queue,
        )
