from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from schemas.schemas import CategoriesResponse
from services.categories_service import get_categories

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("", response_model=CategoriesResponse)
async def get_categories_endpoint(
    language: str = Query(..., description='Idioma ("es" o "en")'),
    name: Optional[str] = Query(None),
    id: Optional[int] = Query(None),
) -> CategoriesResponse:
    """List categories via the service layer."""
    try:
        return await get_categories(language, name=name, id=id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

