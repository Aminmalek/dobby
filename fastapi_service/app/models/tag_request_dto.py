from pydantic import BaseModel

class TagRequestDTO(BaseModel):
    doc_id: str
    tag: int
