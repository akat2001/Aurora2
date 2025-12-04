import asyncio
from app.db.database import engine, Base
from app.models import user_models  # importa o módulo para registrar as tabelas

async def init_models():
    async with engine.begin() as conn:
        # Cria todas as tabelas que ainda não existem
        await conn.run_sync(Base.metadata.create_all)
    print("Tabelas de usuário e pessoa criadas com sucesso!")

if __name__ == "__main__":
    asyncio.run(init_models())
