from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.models.base import Base

DATABASE_URL = "postgresql+asyncpg://postgres:1234@127.0.0.1/aurora"

# Engine async
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Sessão async
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Função utilitária para criar todas as tabelas
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
