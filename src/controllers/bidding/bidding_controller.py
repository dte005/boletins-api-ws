from src.environment import env
from src.errors_handlers import BusinessException
from src.services import AzureDataTableService, PublisherBidding

from ...schemas import BiddingRequestDto, BiddingResponseDto, WorkerStatusDto


class BiddingController:
    publisher: PublisherBidding
    table_name: str
    partition_key: str

    def __init__(self):
        self.publisher = PublisherBidding()
        self.table_name = env("AZURE_TABLE_NAME", "")
        self.partition_key = env("PARTITION_KEY_BIDDING", "")

    def send(self, params: BiddingRequestDto) -> BiddingResponseDto:
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
        return BiddingResponseDto(
            id=id,
            status=worker_status.status,
            queue_name="bidding",
            task_name="rpa.bidding",
        )
