from celery import Celery

from src.environment import env

# responsible to send tasks
celery_app = Celery("sender")
broker = env("CELERY_BROKER_URL", "")

celery_app.conf.update(
    broker_url=broker,
    broker_connection_retry_on_startup=True,
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
)
