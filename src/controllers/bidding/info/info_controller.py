from src.environment import env
from src.services.celery.publishers.bulletin.bulletin_publisher import Publisher


class InfoController:
    publisher: Publisher
    table_name: str
    partition_key: str

    def __init__(self):
        self.publisher = Publisher()
        self.table_name = env("AZURE_TABLE_NAME", "")
        self.partition_key = "bidding"
