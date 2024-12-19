from fastapi import Query
from pydantic import BaseModel

class SearchRequestDTO(BaseModel):
    field: str = Query(...),
    value: str = Query(...)