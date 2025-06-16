from typing import Optional

from database import database

async def list_orders(user_id: Optional[str] = None, id: Optional[int] = None) -> list[dict]:
    """Fetch orders filtered by user_id or id."""
    query = "SELECT * FROM orders"
    conditions = []
    params: dict[str, object] = {}
    if user_id is not None:
        conditions.append("user_id = :user_id")
        params["user_id"] = user_id
    if id is not None:
        conditions.append("id = :id")
        params["id"] = id
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    return await database.fetch_all(query, params)
