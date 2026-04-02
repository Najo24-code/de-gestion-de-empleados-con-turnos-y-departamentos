"""
De Gestion De Empleados Con Turnos Y Departamentos - API REST

"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from database import init_db
from auth import router as auth_router
from routes.items import router as items_router
from routes.export import router as export_router

app = FastAPI(
    title="De Gestion De Empleados Con Turnos Y Departamentos",
    description="API REST con autenticación JWT",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"status": "ok", "project": "De Gestion De Empleados Con Turnos Y Departamentos", "docs": "/docs"}

@app.get("/health")
def health():
    return {"status": "healthy"}

# Routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(export_router, prefix="/export", tags=["export"])

# Servir frontend
@app.get("/app")
def serve_frontend():
    return FileResponse("frontend/index.html")
