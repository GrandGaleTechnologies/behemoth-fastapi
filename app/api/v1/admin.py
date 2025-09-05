from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.models.user import User
from app.schemas.auth import UserOut
from app.auth import get_current_user

# Admin router
router = APIRouter(prefix="/admin", tags=["Admin"])

# Dependency to ensure user is admin
async def get_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    return current_user

# Endpoint: list all users
@router.get("/users", response_model=list[UserOut])
async def list_users(db: AsyncSession = Depends(get_db), admin_user: User = Depends(get_admin_user)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users
