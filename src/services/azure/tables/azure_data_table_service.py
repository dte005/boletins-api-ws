import logging

from azure.data.tables import TableClient, TableServiceClient

from src.environment import env
from src.schemas.worker_dto import WorkerStatusDto

logger = logging.getLogger(__name__)


class AzureDataTableService:
    service: TableServiceClient
    table: TableClient
    conn_str: str

    def __init__(self, table_name: str) -> None:
        self.conn_str = env("AZURE_STORAGE_CONNECTION_STRING", "")
        if self.conn_str is None:
            raise ValueError("AZURE_STORAGE_CONNECTION_STRING must be set")
        self.service = TableServiceClient.from_connection_string(
            conn_str=self.conn_str,
        )
        self.table = self.service.get_table_client(table_name=table_name)

    def post(self, params: WorkerStatusDto) -> None:
        self.table.upsert_entity(entity=params.model_dump(mode="json"))
        self.service.close()
