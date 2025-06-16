from typing import Optional

from database import database

async def list_users(email: Optional[str] = None, id: Optional[int] = None) -> list[dict]:
    """Fetch users filtered by email or id."""
    query = "SELECT * FROM users"
    conditions = []
    params: dict[str, object] = {}
    if email is not None:
        conditions.append("email = :email")
        params["email"] = email
    if id is not None:
        conditions.append("id = :id")
        params["id"] = id
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    return await database.fetch_all(query, params)
