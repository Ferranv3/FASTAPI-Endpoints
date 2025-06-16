from typing import Optional

from repositories.categories import list_categories
from schemas.schemas import CategoriesResponse, Category
from .common import validate_language

async def get_categories(language: str, name: Optional[str] = None, id: Optional[int] = None) -> CategoriesResponse:
    """Return categories response after validating language."""
    validate_language(language)
    rows = await list_categories(name=name, id=id)
    return CategoriesResponse(total=len(rows), categories=[Category(**row) for row in rows])
