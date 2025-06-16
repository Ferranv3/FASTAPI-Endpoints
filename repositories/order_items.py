from typing import Optional

from database import database

async def list_order_items(order_id: Optional[str] = None, id: Optional[int] = None) -> list[dict]:
    """Fetch order items filtered by order_id or id."""
    query = "SELECT * FROM order_items"
    conditions = []
    params: dict[str, object] = {}
    if order_id is not None:
        conditions.append("order_id = :order_id")
        params["order_id"] = order_id
    if id is not None:
        conditions.append("id = :id")
        params["id"] = id
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    return await database.fetch_all(query, params)
