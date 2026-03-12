from fastapi import FastAPI
from .api import routers
from .db.database import engine
from contextlib import asynccontextmanager
from sqlalchemy import text
from .utils.constants import ROUTES

app = FastAPI(
    title="Internship Portal API",
    description="This is the Internship Portal API developed by Al-Khair Pama. It handles user management, job postings, and more.",
)


for router, (name, tags) in zip(routers["v1"], ROUTES):
    app.include_router(router=router, prefix=f"/api/v1/{name}")


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.on_event("startup")
def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT NOW()"))
        print("✅ Database connected:", result.scalar())
