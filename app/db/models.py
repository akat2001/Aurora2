# app/db/models.py
from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from .database import Base

class Pessoa(Base):
    __tablename__ = "pessoa"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    sexo = Column(String(15))
    data_nascimento = Column(Date)
    telefone = Column(String(20))
    cidade_id = Column(Integer)  # ou ForeignKey("cidade.id") se tiver tabela de cidades
    created_at = Column(TIMESTAMP, server_default="now()")
    updated_at = Column(TIMESTAMP, server_default="now()")

    usuario = relationship("Usuario", back_populates="pessoa", uselist=False)

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(128), nullable=False)
    usernick = Column(String(50), nullable=False, unique=True)
    pessoa_id = Column(Integer, ForeignKey("pessoa.id"), nullable=False)
    verificado = Column(Boolean, default=False)
    codigo_verificacao = Column(String(64))
    last_access = Column(TIMESTAMP)
    created_at = Column(TIMESTAMP, server_default="now()")
    updated_at = Column(TIMESTAMP, server_default="now()")

    pessoa = relationship("Pessoa", back_populates="usuario")
