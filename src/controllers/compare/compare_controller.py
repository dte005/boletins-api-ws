import logging

from src.environment import env
from src.errors_handlers import BusinessException

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
        service = AzureDataTableService(table_name=self.table_name)
        # Jogar na fila em cloud, gerando o id de identificação
        result = self.publisher.task(params)
        id = result.id if result is not None and result.id is not None else ""
        if not id:
            raise BusinessException("Failed to get task id")

        worker_status = WorkerStatusDto(
            PartitionKey=self.partition_key,
            RowKey=id,
            status=result.status,
            request_content=str(params.model_dump_json()),
        )
        # Atualizar o Table content na azure com o status
        service.post(worker_status)
        # retornar o id de identificação
        return CompareResponseDto(
            id=id,
            status=worker_status.status,
            queue_name="compare",
            task_name="rpa.compare",
        )
