from typing import Optional

from repositories.products import list_products
from schemas.schemas import ProductsResponse, Product
from .common import validate_language

async def get_products(language: str, name: Optional[str] = None, id: Optional[int] = None) -> ProductsResponse:
    """Return products response after validating language."""
    validate_language(language)
    rows = await list_products(name=name, id=id)
    return ProductsResponse(total=len(rows), products=[Product(**row) for row in rows])
