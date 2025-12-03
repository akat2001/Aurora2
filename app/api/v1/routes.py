from fastapi import APIRouter
from sqlalchemy import insert, select
from app.db.database import engine
from app.db.models import test_table

router = APIRouter()

# Rota para inserir um dado de teste
@router.post("/test_insert/")
async def test_insert(name: str):
    with engine.begin() as conn:  # usando 'with' porque seu engine é síncrono
        result = conn.execute(insert(test_table).values(name=name))
        conn.commit()
    return {"message": f"Dado '{name}' inserido com sucesso!"}

# Rota para ler dados de teste
@router.get("/test_read/")
async def test_read():
    with engine.begin() as conn:
        result = conn.execute(select(test_table))
        rows = [{"id": row.id, "name": row.name} for row in result]
    return rows
