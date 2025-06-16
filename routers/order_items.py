from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from schemas.schemas import OrderItemsResponse
from services.order_items_service import get_order_items

router = APIRouter(
    prefix="/orderItems",
    tags=["order_items"]
)

@router.get("/", response_model=OrderItemsResponse)
async def get_order_items_endpoint(
    language: str = Query(..., description='Idioma ("es" o "en")'),
    order_id: Optional[str] = Query(None),
    id: Optional[int] = Query(None),
) -> OrderItemsResponse:
    """List order items via the service layer."""
    try:
        return await get_order_items(language, order_id=order_id, id=id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

