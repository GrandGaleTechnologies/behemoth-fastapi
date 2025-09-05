from pydantic import BaseModel, EmailStr
from typing import Optional


# Base user info shared across schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr


# Schema for creating a new user (signup)
class UserCreate(UserBase):
    password: str  # plain password from request


# Schema for login request
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# Schema for returning user info (response)
class UserOut(UserBase):
    id: int
    role: str

    class Config:
        from_attributes = True  # for ORM compatibility


# JWT token schema
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Optional data inside JWT
class TokenData(BaseModel):
    id: Optional[int] = None
    email: Optional[EmailStr] = None


# Schema for responses on signup/login success
class AuthResponse(BaseModel):
    status: str = "success"
    message: Optional[str] = None
    data: Optional[UserOut] = None
    token: Optional[Token] = None
