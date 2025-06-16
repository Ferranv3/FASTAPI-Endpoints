from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from schemas.schemas import ProductsResponse
from services.products_service import get_products

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("", response_model=ProductsResponse)
async def get_products_endpoint(
    language: str = Query(..., description='Idioma ("es" o "en")'),
    name: Optional[str] = Query(None),
    id: Optional[int] = Query(None),
) -> ProductsResponse:
    """List products via the service layer."""
    try:
        return await get_products(language, name=name, id=id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

