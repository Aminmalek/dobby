from fastapi import APIRouter
from models.tag_request_dto import TagRequestDTO
from services.tag_service import TagService
from config.settings import settings

router = APIRouter()
tag_service = TagService()

@router.post("/tag/")
async def tag_content(request: TagRequestDTO):
    return tag_service.tag_content(
        index=settings.TEXTS_INDEX, 
        doc_id=request.doc_id, 
        tag=request.tag
    )
