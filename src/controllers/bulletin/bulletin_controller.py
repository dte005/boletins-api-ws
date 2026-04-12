import logging
from uuid import uuid4

from src.environment import env

from ...schemas import BulletinRequestDto, BulletinResponseDto, WorkerStatusDto
from ...services import AzureDataTableService, PublisherBulletin

logger = logging.getLogger(__name__)


class BulletinController:
    publisher: PublisherBulletin
    table_name: str
    partition_key: str

    def __init__(self):
        self.publisher = PublisherBulletin()
        self.table_name = env("AZURE_TABLE_NAME", "")
        self.partition_key = env("PARTITION_KEY_BULLETIN", "")

    def send(self, params: BulletinRequestDto) -> BulletinResponseDto:
        task_id = str(uuid4())
        service = AzureDataTableService(table_name=self.table_name)
        params.task_id = task_id

        worker_status = WorkerStatusDto(
            PartitionKey=self.partition_key,
            RowKey=task_id,
            request_content=str(params.model_dump_json()),
        )
        # Atualizar o Table content na azure com o status
        service.post(worker_status)

        # Jogar na fila em cloud
        self.publisher.task(params)

        return BulletinResponseDto(
            id=task_id,
            status=worker_status.status,
            queue_name="bulletin",
            task_name="rpa.bulletin",
        )
