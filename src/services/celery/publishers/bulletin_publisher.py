from src.environment import env
from src.services.celery.celery import celery_app


def publish_task(params: dict):
    queue = env("QUEUE_BULLETIN", "")
    result = celery_app.send_task(
        "rpa.bulletin",
        args=[
            {
                "period": params.get("period", ""),
                "target_date": params.get("target_date", ""),
            }
        ],
        queue=queue,
    )
    return {
        "task_id": result.id,
        "task_name": "rpa.bulletin",
        "queue": queue,
    }
