from fastapi import FastAPI
from .api import routers
from .db.database import engine
from contextlib import asynccontextmanager
from sqlalchemy import text


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Code to run at startup
#     async with engine.connect() as conn:
#         result = await conn.execute(text("SELECT NOW()"))
#         print("✅ Database connected. Current time:", result.scalar())
#     yield
#     # Code to run at shutdown (optional)
#     print("App is shutting down...")


app = FastAPI(
    title="Internship Portal API",
    description="This is the Internship Portal API developed by Al-Khair Pama. It handles user management, job postings, and more.",
)


ROUTES = [("interns", "Interns"), ("companies", "Companies")]


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
