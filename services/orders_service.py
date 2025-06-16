from typing import Optional

from repositories.orders import list_orders
from schemas.schemas import OrdersResponse, Order
from .common import validate_language

async def get_orders(language: str, user_id: Optional[str] = None, id: Optional[int] = None) -> OrdersResponse:
    """Return orders response after validating language."""
    validate_language(language)
    rows = await list_orders(user_id=user_id, id=id)
    return OrdersResponse(total=len(rows), orders=[Order(**row) for row in rows])
