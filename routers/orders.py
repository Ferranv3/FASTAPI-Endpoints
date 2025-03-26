from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from database import database
from schemas.schemas import OrdersResponse

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get("", response_model = OrdersResponse)
async def get_orders(language: str = Query(..., description='Idioma ("es" o "en")'),
                      user_id: Optional[str] = Query(None),
                      id: Optional[int] = Query(None)):
    
    if language not in ["es", "en"]:
        raise HTTPException(status_code=400, detail="Idioma no válido")

    query = "SELECT * FROM orders"
    conditions = []
    params = {}

    if user_id:
        conditions.append("user_id = :user_id")
        params["user_id"] = user_id
    
    if id:
        conditions.append("id = :id")
        params["id"] = id

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    print("Query: " + query)
    print(f"Params: {params}")
    
    rows = await database.fetch_all(query, params)
    
    print(f"Rows: {rows}")
    return {"total": len(rows), "orders": rows}
