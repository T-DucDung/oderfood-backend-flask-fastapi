
from typing import List, Optional

from pydantic import BaseModel


class RegisterBase(BaseModel):
    id: int
    name: str
    password: str
    email: str
    sex: str
    country: str

class Register(RegisterBase):
    id: int
    name: str
    name: str
    password: str
    email: str
    sex: str
    country: str
    
    class Config:
        orm_mode = True