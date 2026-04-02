"""CSV Export"""
import csv
import io
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from database import get_db
from models import User, Turno, Departamento
from auth import get_current_user

router = APIRouter()

@router.get("/turnos/csv")
def export_turnos_csv(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    items = db.query(Turno).filter(Turno.owner_id == current_user.id).all()
    cols  = [c.key for c in Turno.__table__.columns]
    buf   = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(cols)
    for item in items:
        writer.writerow([getattr(item, c, "") for c in cols])
    buf.seek(0)
    return StreamingResponse(
        io.BytesIO(buf.getvalue().encode("utf-8")),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=turnos.csv"}
    )

@router.get("/departamentos/csv")
def export_departamentos_csv(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    items = db.query(Departamento).filter(Departamento.owner_id == current_user.id).all()
    cols  = [c.key for c in Departamento.__table__.columns]
    buf   = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(cols)
    for item in items:
        writer.writerow([getattr(item, c, "") for c in cols])
    buf.seek(0)
    return StreamingResponse(
        io.BytesIO(buf.getvalue().encode("utf-8")),
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": "attachment; filename=departamentos.csv"}
    )
