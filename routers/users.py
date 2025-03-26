from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from database import database
from schemas.schemas import UsersResponse

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("", response_model = UsersResponse)
async def get_users(language: str = Query(..., description='Idioma ("es" o "en")'),
                          email: Optional[str] = Query(None),
                          id: Optional[int] = Query(None)):
    
    if language not in ["es", "en"]:
        raise HTTPException(status_code=400, detail="Idioma no válido")

    query = "SELECT * FROM users"
    conditions = []
    params = {}

    if email:
        conditions.append("email = :email")
        params["email"] = email
    
    if id:
        conditions.append("id = :id")
        params["id"] = id

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    print("Query: " + query)
    print(f"Params: {params}")
    
    rows = await database.fetch_all(query, params)
    
    print(f"Rows: {rows}")
    return {"total": len(rows), "users": rows}
