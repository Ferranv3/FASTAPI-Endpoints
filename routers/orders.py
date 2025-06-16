from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from schemas.schemas import OrdersResponse
from services.orders_service import get_orders

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get("", response_model=OrdersResponse)
async def get_orders_endpoint(
    language: str = Query(..., description='Idioma ("es" o "en")'),
    user_id: Optional[str] = Query(None),
    id: Optional[int] = Query(None),
) -> OrdersResponse:
    """List orders via the service layer."""
    try:
        return await get_orders(language, user_id=user_id, id=id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

