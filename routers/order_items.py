from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from database import database
from schemas.schemas import OrderItemsResponse

router = APIRouter(
    prefix="/orderItems",
    tags=["order_items"]
)

@router.get("/", response_model = OrderItemsResponse)
async def get_order_items(language: str = Query(..., description='Idioma ("es" o "en")'),
                            order_id: Optional[str] = Query(None),
                            id: Optional[int] = Query(None)):
    
    if language not in ["es", "en"]:
        raise HTTPException(status_code=400, detail="Idioma no válido")

    query = "SELECT * FROM order_items"
    conditions = []
    params = {}

    if order_id:
        conditions.append("order_id = :order_id")
        params["order_id"] = order_id
    
    if id:
        conditions.append("id = :id")
        params["id"] = id

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    print("Query: " + query)
    print(f"Params: {params}")
    
    rows = await database.fetch_all(query, params)
    
    print(f"Rows: {rows}")
    return {"total": len(rows), "order_items": rows}
