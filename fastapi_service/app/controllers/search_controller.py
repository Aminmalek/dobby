from config.settings import settings
from fastapi import APIRouter, Query
from services.search_service import SearchService

router = APIRouter()

# Dependency Injection of the Elasticsearch repository and the search service
search_service = SearchService(settings.ELASTIC_HOST, index=settings.TEXTS_INDEX)


@router.get("/search/")
async def search_content(field: str = Query(...),  # Query parameter for field
                         value: str = Query(...)):
    results = search_service.search(field=field, value=value)
    return results
