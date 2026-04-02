from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from auth import get_current_user
from models import User, Turno, Departamento
from schemas import UserCreate, UserResponse, TurnoCreate, TurnoUpdate, TurnoResponse, DepartamentoCreate, DepartamentoUpdate, DepartamentoResponse

router = APIRouter()

@router.get("/", response_model=List[TurnoResponse])
async def read_turnos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    turnos = db.query(Turno).filter(Turno.owner_id == current_user.id).all()
    return turnos

@router.post("/", response_model=TurnoResponse)
async def create_turno(turno: TurnoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_turno = Turno(nombre=turno.nombre, descripcion=turno.descripcion, owner_id=current_user.id)
    db.add(db_turno)
    db.commit()
    db.refresh(db_turno)
    return db_turno

@router.get("/{turno_id}", response_model=TurnoResponse)
async def read_turno(turno_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    turno = db.query(Turno).filter(Turno.id == turno_id).filter(Turno.owner_id == current_user.id).first()
    if turno is None:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return turno

@router.put("/{turno_id}", response_model=TurnoResponse)
async def update_turno(turno_id: int, turno: TurnoUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_turno = db.query(Turno).filter(Turno.id == turno_id).filter(Turno.owner_id == current_user.id).first()
    if db_turno is None:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    if turno.nombre:
        db_turno.nombre = turno.nombre
    if turno.descripcion:
        db_turno.descripcion = turno.descripcion
    db.commit()
    db.refresh(db_turno)
    return db_turno

@router.delete("/{turno_id}")
async def delete_turno(turno_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    turno = db.query(Turno).filter(Turno.id == turno_id).filter(Turno.owner_id == current_user.id).first()
    if turno is None:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    db.delete(turno)
    db.commit()
    return {"message": "Turno eliminado"}

@router.get("/departamentos/", response_model=List[DepartamentoResponse])
async def read_departamentos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    departamentos = db.query(Departamento).filter(Departamento.owner_id == current_user.id).all()
    return departamentos

@router.post("/departamentos/", response_model=DepartamentoResponse)
async def create_departamento(departamento: DepartamentoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_departamento = Departamento(nombre=departamento.nombre, descripcion=departamento.descripcion, owner_id=current_user.id)
    db.add(db_departamento)
    db.commit()
    db.refresh(db_departamento)
    return db_departamento

@router.get("/departamentos/{departamento_id}", response_model=DepartamentoResponse)
async def read_departamento(departamento_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    departamento = db.query(Departamento).filter(Departamento.id == departamento_id).filter(Departamento.owner_id == current_user.id).first()
    if departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    return departamento

@router.put("/departamentos/{departamento_id}", response_model=DepartamentoResponse)
async def update_departamento(departamento_id: int, departamento: DepartamentoUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_departamento = db.query(Departamento).filter(Departamento.id == departamento_id).filter(Departamento.owner_id == current_user.id).first()
    if db_departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    if departamento.nombre:
        db_departamento.nombre = departamento.nombre
    if departamento.descripcion:
        db_departamento.descripcion = departamento.descripcion
    db.commit()
    db.refresh(db_departamento)
    return db_departamento

@router.delete("/departamentos/{departamento_id}")
async def delete_departamento(departamento_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    departamento = db.query(Departamento).filter(Departamento.id == departamento_id).filter(Departamento.owner_id == current_user.id).first()
    if departamento is None:
        raise HTTPException(status_code=404, detail="Departamento no encontrado")
    db.delete(departamento)
    db.commit()
    return {"message": "Departamento eliminado"}