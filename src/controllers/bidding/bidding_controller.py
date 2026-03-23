from uuid import uuid4

from src.environment import env
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
        task_id = str(uuid4())
        params.task_id = task_id
        service = AzureDataTableService(table_name=self.table_name)
        # Jogar na fila em cloud, gerando o id de identificação

        worker_status = WorkerStatusDto(
            PartitionKey=self.partition_key,
            RowKey=task_id,
            request_content=str(params.model_dump_json()),
        )
        # Atualizar o Table content na azure com o status
        service.post(worker_status)

        self.publisher.task(params)
        # retornar o id de identificação
        return BiddingResponseDto(
            id=task_id,
            status=worker_status.status,
            queue_name="bidding",
            task_name="rpa.bidding",
        )
