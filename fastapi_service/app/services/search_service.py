from repositories.elastic_repository import ElasticRepository

class SearchService:
    def __init__(self):
        self.elastic_repo = ElasticRepository()

from elasticsearch import Elasticsearch


class SearchService:
    def __init__(self, host: str, index: str):
        self.client = Elasticsearch(host)
        self.index = index
    def initialize_data(self):
        """Insert initial mock data into Elasticsearch."""
        mock_data = [
            {
                "_id": "LyrH3pMBUWdzd634tRpC",
                "_source": {
                    "title": "افتاده..",
                    "author": "گلی فولادوند",
                    "genre": "Atque",
                    "content": "تعدادی توپ در اختیار من نبود و ربع ساعت‌های تفریح نتوانند بخندند، سر کلاس، بچه‌های مردم می‌آن این جا آقا و.",
                    "inserted_at": "2024-12-19T11:57:30.305180"
                }
            },
            {
                "_id": "MCrH3pMBUWdzd634tRpR",
                "_source": {
                    "title": "از موعد.",
                    "author": "روئین بدخشانی",
                    "genre": "At",
                    "content": "می‌شدم. حضور این ولی طفل گیجم کرده بود و ما ورقه‌ی انجام کارش را به کاری مشغول کردم که علت، پول تو جیبی داره.",
                    "inserted_at": "2024-12-19T11:57:30.319432"
                }
            }
        ]
        for data in mock_data:
            self.client.index(index=self.index, id=data["_id"], body=data["_source"])

    def search(self, field: str, value: str):
        # body = {
        #     "query": {
        #         "bool": {
        #             "must": [
        #                 {"multi_match": {
        #                     "query": query,  # User query
        #                     "fields": ["title", "author", "genre", "content", "inserted_at"]  # Search across these fields
        #                 }}
        #             ]
        #         }
        #     }
        # }
        body = {
            "query": {
                "match": {
                    field: value
                }
            }
        }
        response = self.client.search(index="texts_index", body=body)
        return response

    class ElasticService:
        def __init__(self, es_server: str, index_name: str):
            self.es = Elasticsearch([es_server])
            self.index_name = index_name

        def search(self, field: str, query: str):
            body = {"query": {"match": {field: query}}}
            results = self.es.search(index=self.index_name, body=body)
            return results["hits"]["hits"]

        def tag_content(self, doc_id: str, tag: int):
            body = {"doc": {"Tag": tag}}
            self.es.update(index=self.index_name, id=doc_id, body=body)
            return {"status": "updated", "tag": tag}