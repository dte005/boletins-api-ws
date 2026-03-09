from azure.data.tables import TableClient, TableServiceClient

from src.environment import env
from src.schemas.worker_dto import WorkerStatusDto


class AzureDataTablesService:
    service: TableServiceClient
    table: TableClient

    def __init__(self, table_name: str) -> None:
        conn_str = env("AZURE_STORAGE_CONNECTION_STRING", "")
        if conn_str is None:
            raise ValueError(
                "AZURE_STORAGE_CONNECTION_STRING and AZURE_TABLE_NAME must be set"
            )
        self.service = TableServiceClient.from_connection_string(
            conn_str=env("AZURE_STORAGE_CONNECTION_STRING", ""),
        )
        self.table = self.service.get_table_client(table_name=table_name)

    def post(self, params: WorkerStatusDto) -> None:
        self.table.update_entity(entity=params.model_dump(mode="json"))
