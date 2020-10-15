
from typing import List, Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    content: str

class UserCreate(UserBase):
    content: str

class User(UserBase):
    id: int
    content: str

    class Config:
        orm_mode = True