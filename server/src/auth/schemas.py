from fastapi_users import schemas
from pydantic import EmailStr
from typing import Optional


class UserRead(schemas.BaseUser[int]):
    id: int
    email: EmailStr
    username: str
    is_active: bool
    is_verified: bool
    is_superuser: bool

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    email: EmailStr
    username: str
    password: str
    is_active: Optional[bool] = True
    is_verified: Optional[bool] = False
    is_superuser: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    email: Optional[EmailStr]
    password: Optional[str]
    username: Optional[str]
    is_active: Optional[bool]
    is_verified: Optional[bool]
    is_superuser: Optional[bool]
