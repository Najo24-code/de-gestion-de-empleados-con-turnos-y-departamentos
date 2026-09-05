<code>employee-management-api</code>

# Employee Management System with Shifts and Departments

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white&style=flat-square&labelColor=0d1117)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white&style=flat-square&labelColor=0d1117)](https://fastapi.tiangolo.com/)
[![JWT Auth](https://img.shields.io/badge/JWT-Auth-orange?style=flat-square&labelColor=0d1117)](https://jwt.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white&style=flat-square&labelColor=0d1117)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square&labelColor=0d1117)](LICENSE)

A RESTful API for managing employees, shifts, and departments with user authentication, multi-entity CRUD operations, CSV export, and a responsive SPA frontend. Built with FastAPI, SQLAlchemy, and JWT authentication.

---

## $ quickstart

### Docker (recommended)

```bash
git clone https://github.com/Najo24-code/de-gestion-de-empleados-con-turnos-y-departamentos.git
cd de-gestion-de-empleados-con-turnos-y-departamentos
docker-compose up -d
```

Open http://localhost:8000

### Manual

```bash
git clone https://github.com/Najo24-code/de-gestion-de-empleados-con-turnos-y-departamentos.git
cd de-gestion-de-empleados-con-turnos-y-departamentos

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

uvicorn main:app --reload
```

---

## $ tree

```
de-gestion-de-empleados-con-turnos-y-departamentos/
├── main.py              # FastAPI entry point
├── auth.py              # JWT authentication
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── database.py          # Database configuration
├── routes/
│   ├── __init__.py
│   ├── items.py         # Shifts & Departments CRUD
│   └── export.py        # CSV export endpoints
├── frontend/
│   └── index.html       # SPA frontend
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api.py
├── docs/                # Screenshots
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## $ endpoints

### Authentication

| Method | Endpoint        | Description         |
|--------|-----------------|---------------------|
| POST   | `/auth/register`| Create a new account|
| POST   | `/auth/login`   | Log in and get JWT  |
| GET    | `/auth/me`      | Get current user    |

### Shifts

| Method | Endpoint           | Description         |
|--------|--------------------|---------------------|
| GET    | `/items/`          | List all shifts     |
| POST   | `/items/`          | Create a new shift  |
| GET    | `/items/{id}`      | Get shift by ID     |
| PUT    | `/items/{id}`      | Update a shift      |
| DELETE | `/items/{id}`      | Delete a shift      |

### Departments

| Method | Endpoint                  | Description              |
|--------|---------------------------|--------------------------|
| GET    | `/items/departamentos/`   | List all departments     |
| POST   | `/items/departamentos/`   | Create a new department  |
| GET    | `/items/departamentos/{id}`| Get department by ID    |
| PUT    | `/items/departamentos/{id}`| Update a department    |
| DELETE | `/items/departamentos/{id}`| Delete a department    |

### CSV Export

| Method | Endpoint                    | Description              |
|--------|-----------------------------|--------------------------|
| GET    | `/items/turnos/csv`         | Export shifts as CSV     |
| GET    | `/items/departamentos/csv`  | Export departments as CSV|

---

## $ env

| Variable          | Description            | Default                   |
|-------------------|------------------------|---------------------------|
| `DATABASE_URL`    | Database connection URL| `sqlite:///./data/app.db` |
| `JWT_SECRET`      | Secret key for JWT     | *(required)*              |
| `JWT_ALGORITHM`   | JWT signing algorithm  | `HS256`                   |

---

## $ test

```bash
pytest tests/ -v
```

---

## $ docker

```bash
# Build
docker build -t employee-management-api .

# Run
docker run -p 8000:8000 employee-management-api
```

---

## $ license

MIT © 2026 [Najo24-code](https://github.com/Najo24-code)
