from src.environment import env
from src.services.celery.celery import celery_app


def publish_task(params: dict):
    queue = env("QUEUE_BIDDING", "")
    result = celery_app.send_task(
        "rpa.bidding",
        args=[
            {
                "bidding_id": params.get("bidding_id", ""),
            }
        ],
        queue=queue,
    )
    return {
        "task_id": result.id,
        "task_name": "rpa.bidding",
        "queue": queue,
    }
