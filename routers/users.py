from fastapi import APIRouter, HTTPException, Query
from typing import Optional

from schemas.schemas import UsersResponse
from services.users_service import get_users

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("", response_model=UsersResponse)
async def get_users_endpoint(
    language: str = Query(..., description='Idioma ("es" o "en")'),
    email: Optional[str] = Query(None),
    id: Optional[int] = Query(None),
) -> UsersResponse:
    """List users via the service layer."""
    try:
        return await get_users(language, email=email, id=id)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

