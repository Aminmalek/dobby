from repositories.elastic_repository import ElasticRepository

class TagService:
    def __init__(self):
        self.elastic_repo = ElasticRepository()

    def tag_content(self, index: str, doc_id: str, tag: int):
        body = {
            "doc": {
                "tags": [tag]
            }
        }
        self.elastic_repo.update(index=index, doc_id=doc_id, body=body)
        return {"message": f"Document {doc_id} tagged with {tag}"}
