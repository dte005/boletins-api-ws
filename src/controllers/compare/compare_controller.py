import logging
from uuid import uuid4
from src.environment import env

from ...schemas import CompareRequestDto, CompareResponseDto, WorkerStatusDto
from ...services import AzureDataTableService, PublisherCompare

logger = logging.getLogger(__name__)


class CompareController:
    publisher: PublisherCompare
    table_name: str
    partition_key: str

    def __init__(self):
        self.publisher = PublisherCompare()
        self.table_name = env("AZURE_TABLE_NAME", "")
        self.partition_key = env("PARTITION_KEY_COMPARE", "")

    def send(self, params: CompareRequestDto) -> CompareResponseDto:
        task_id = str(uuid4())
        service = AzureDataTableService(table_name=self.table_name)
        params.task_id = task_id

        worker_status = WorkerStatusDto(
            PartitionKey = self.partition_key,
            RowKey = task_id,
            request_content = str(params.model_dump_json()),
            )
        # Atualizar o Table content na azure com o status
        service.post(worker_status)

        self.publisher.task(params)
        # retornar o id de identificação
        return CompareResponseDto(
            id=task_id,
            status=worker_status.status,
            queue_name="compare",
            task_name="rpa.compare",
        )
