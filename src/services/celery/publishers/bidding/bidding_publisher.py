from src.environment import env
from src.schemas.bidding_dto import BiddingRequestDto, BiddingResponseDto
from src.schemas.domains import WorkerStatus
from src.services.celery.celery import celery_app


class Publisher:
    queue: str
    task_name: str = "rpa.bidding"

    def __init__(self):
        self.queue = env("QUEUE_BIDDING", "")

    def task(self, params: BiddingRequestDto) -> BiddingResponseDto:

        result = celery_app.send_task(
            self.task_name,
            args=[params.model_dump(mode="json")],
            queue=self.queue,
        )

        return BiddingResponseDto(
            id=result.id,
            status=WorkerStatus.progress,
            task_name=self.task_name,
            queue_name=self.queue,
        )
