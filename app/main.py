from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncEngine
from app.db.database import engine, Base
from app.db.models import Usuario

app = FastAPI()

@app.on_event("startup")
async def startup():
    # Criar tabelas se não existirem
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def root():
    return {"message": "API funcionando!"}
