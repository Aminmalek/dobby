from elasticsearch import Elasticsearch
from config.settings import settings

class ElasticRepository:
    def __init__(self):
        self.client = Elasticsearch(settings.ELASTIC_HOST)

    def search(self, index: str, query: dict):
        return self.client.search(index=index, body=query)

    def update(self, index: str, doc_id: str, body: dict):
        return self.client.update(index=index, id=doc_id, body=body)
