from typing import Optional

from repositories.users import list_users
from schemas.schemas import UsersResponse, User
from .common import validate_language

async def get_users(language: str, email: Optional[str] = None, id: Optional[int] = None) -> UsersResponse:
    """Return users response after validating language."""
    validate_language(language)
    rows = await list_users(email=email, id=id)
    return UsersResponse(total=len(rows), users=[User(**row) for row in rows])
