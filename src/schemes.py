from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

# Схема для создания нового пользователя
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

# Схема для отображения информации о пользователе
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

# Схема для обновления данных пользователя
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr]
    password: Optional[str] = Field(None, min_length=6)

# Схема для создания поста
class PostCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)
    tags: List[str]

# Схема для отображения информации о посте
class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    author: UserResponse

    class Config:
        orm_mode = True
        
# Схема для списка постов
class PostListResponse(BaseModel):
    posts: List[PostResponse]
    total: int