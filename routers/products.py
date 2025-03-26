from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from database import database
from schemas.schemas import ProductsResponse

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

@router.get("", response_model = ProductsResponse)
async def get_products(language: str = Query(..., description='Idioma ("es" o "en")'),
                      name: Optional[str] = Query(None),
                      id: Optional[int] = Query(None)):

    if language not in ["es", "en"]:
        raise HTTPException(status_code=400, detail="Idioma no válido")
    
    query = "SELECT * FROM products"
    conditions = []
    params = {}

    if name:
        conditions.append("name = :name")
        params["name"] = name
    
    if id:
        conditions.append("id = :id")
        params["id"] = id

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    print("Query: " + query)
    print(f"Params: {params}")
    
    rows = await database.fetch_all(query, params)
    
    print(f"Rows: {rows}")
    return {"total": len(rows), "products": rows}