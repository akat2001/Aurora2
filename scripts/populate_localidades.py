import asyncio
import asyncpg
import requests

DB_CONFIG = {
    "user": "postgres",
    "password": "1234",
    "database": "aurora",
    "host": "localhost",
    "port": 5432
}

async def populate_localidades():
    conn = await asyncpg.connect(**DB_CONFIG)
    
    # Criar tabelas caso não existam
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS estados (
        id INT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        sigla CHAR(2) NOT NULL
    );
    """)
    
    await conn.execute("""
    CREATE TABLE IF NOT EXISTS cidades (
        id INT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        estado_id INT NOT NULL REFERENCES estados(id)
    );
    """)

    # 1️⃣ Popular estados
    estados = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados").json()
    for estado in estados:
        await conn.execute("""
            INSERT INTO estados (id, nome, sigla)
            VALUES ($1, $2, $3)
            ON CONFLICT (id) DO NOTHING
        """, estado["id"], estado["nome"], estado["sigla"])
    
    # 2️⃣ Popular cidades
    for estado in estados:
        cidades = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado['id']}/municipios").json()
        for cidade in cidades:
            await conn.execute("""
                INSERT INTO cidades (id, nome, estado_id)
                VALUES ($1, $2, $3)
                ON CONFLICT (id) DO NOTHING
            """, cidade["id"], cidade["nome"], estado["id"])
    
    await conn.close()
    print("Estados e cidades populados com sucesso!")

if __name__ == "__main__":
    asyncio.run(populate_localidades())
