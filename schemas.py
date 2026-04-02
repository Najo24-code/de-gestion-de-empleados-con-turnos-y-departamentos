from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    username: str
    is_active: bool

    class Config:
        from_attributes = True
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TurnoCreate(BaseModel):
    nombre: str
    descripcion: Optional[str]

class TurnoUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]

class TurnoResponse(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str]
    owner_id: int

    class Config:
        from_attributes = True
        from_attributes = True

class DepartamentoCreate(BaseModel):
    nombre: str
    descripcion: Optional[str]

class DepartamentoUpdate(BaseModel):
    nombre: Optional[str]
    descripcion: Optional[str]

class DepartamentoResponse(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str]
    owner_id: int

    class Config:
        from_attributes = True
        from_attributes = True