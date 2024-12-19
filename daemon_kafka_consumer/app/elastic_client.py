from elasticsearch import Elasticsearch
from datetime import datetime

class ElasticClient:
    def __init__(self, host: str, index: str):
        self.client = Elasticsearch(host)
        self.index = index
        self._create_index()

    def _create_index(self):
        if not self.client.indices.exists(index=self.index):
            self.client.indices.create(
                index=self.index,
                body={
                    "mappings": {
                        "properties": {
                            "Name": {"type": "text"},
                            "Username": {"type": "keyword"},
                            "Category": {"type": "keyword"},
                            "Text": {"type": "text"},
                            "Inserted_at": {"type": "date"}
                        }
                    }
                }
            )

    def index_document(self, record):
        record["inserted_at"] = datetime.now().isoformat()
        self.client.index(index=self.index, document=record)
