from pydantic import BaseModel, EmailStr
from typing import Any, Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True  # ✅ allows FastAPI to convert SQLAlchemy objects automatically

# Add this for your sample_module
class ResponseSchema(BaseModel):
    status: str
    data: Optional[Any] = None
    message: Optional[str] = None
