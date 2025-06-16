from typing import Optional

from repositories.order_items import list_order_items
from schemas.schemas import OrderItemsResponse, OrderItem
from .common import validate_language

async def get_order_items(language: str, order_id: Optional[str] = None, id: Optional[int] = None) -> OrderItemsResponse:
    """Return order items response after validating language."""
    validate_language(language)
    rows = await list_order_items(order_id=order_id, id=id)
    return OrderItemsResponse(total=len(rows), order_items=[OrderItem(**row) for row in rows])
