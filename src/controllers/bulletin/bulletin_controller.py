from src.environment import env
from src.errors_handlers import BusinessException
from src.schemas.bulletin_dto import BulletinRequestDto, BulletinResponseDto
from src.schemas.worker_dto import WorkerStatusDto
from src.services.azure.tables.azure_data_table_service import AzureDataTableService
from src.services.celery.publishers.bulletin.bulletin_publisher import Publisher


class BulletinController:
    publisher: Publisher
    table_name: str
    partition_key: str

    def __init__(self):
        self.publisher = Publisher()
        self.table_name = env("AZURE_TABLE_NAME", "")
        self.partition_key = env("PARTITION_KEY_BULLETIN", "")

    def get_bulletin(self, params: BulletinRequestDto) -> BulletinResponseDto:
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
        return BulletinResponseDto(
            id=id,
            status=worker_status.status,
            queue_name="bulletin",
            task_name="rpa.bulletin",
        )
