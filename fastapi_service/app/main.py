# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Optional
# from elasticsearch import Elasticsearch
# from config import ELASTIC_HOST
# # Initialize FastAPI and Elasticsearch client
# app = FastAPI()
# es = Elasticsearch(ELASTIC_HOST)

# class SearchRequest(BaseModel):
#     field: str
#     value: str

# class TagRequest(BaseModel):
#     doc_id: str
#     tag: int

# @app.post("/search/")
# async def search_content(request: SearchRequest):
#     query = {
#         "query": {
#             "match": {request.field: request.value}
#         }
#     }
#     response = es.search(index="texts_index", body=query)
#     return response['hits']['hits']

# @app.post("/tag/")
# async def tag_content(request: TagRequest):
#     doc_id = request.doc_id
#     tag = request.tag
#     es.update(index="texts_index", id=doc_id, body={
#         "doc": {
#             "tags": [tag]
#         }
#     })
#     return {"message": f"Document {doc_id} tagged with {tag}"}
from fastapi import FastAPI
from controllers import search_controller, tag_controller

app = FastAPI()

# Register routes
app.include_router(search_controller.router, prefix="/api")
app.include_router(tag_controller.router, prefix="/api")

