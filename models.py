from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, Text
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    turnos = relationship("Turno", back_populates="owner")
    departamentos = relationship("Departamento", back_populates="owner")

class Turno(Base):
    __tablename__ = "turnos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="turnos")

class Departamento(Base):
    __tablename__ = "departamentos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    descripcion = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="departamentos")