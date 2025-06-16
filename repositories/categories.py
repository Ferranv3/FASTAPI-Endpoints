from typing import Optional

from database import database

async def list_categories(name: Optional[str] = None, id: Optional[int] = None) -> list[dict]:
    """Fetch categories filtered by name or id."""
    query = "SELECT * FROM categories"
    conditions = []
    params: dict[str, object] = {}
    if name is not None:
        conditions.append("name = :name")
        params["name"] = name
    if id is not None:
        conditions.append("id = :id")
        params["id"] = id
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    return await database.fetch_all(query, params)
