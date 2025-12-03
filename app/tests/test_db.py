from app.db.database import SessionLocal
from app.models.user import User

@app.get("/test-db")
async def test_db():
    async with SessionLocal() as session:
        new_user = User(name="Juliane", email="juliane@example.com")
        session.add(new_user)
        await session.commit()

        result = await session.execute("SELECT * FROM users")
        users = result.fetchall()
    return {"users": [dict(u._mapping) for u in users]}
