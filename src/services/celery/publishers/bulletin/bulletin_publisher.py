from src.environment import env
from src.schemas.bulletin_dto import BulletinRequestDto
from src.schemas.domains import WorkerStatus
from src.services.celery.celery import celery_app
from src.services.celery.publishers.schemas.task_dto import TaskResponseDto


def publish_task(params: BulletinRequestDto) -> TaskResponseDto:
    queue = env("QUEUE_BULLETIN", "")
    result = celery_app.send_task(
        "rpa.bulletin",
        args=[params.model_dump(mode="json")],
        queue=queue,
    )

    return TaskResponseDto(
        id=result.id,
        status=WorkerStatus.progress.name,
        task_name="rpa.bulletin",
        queue_name=queue,
    )
