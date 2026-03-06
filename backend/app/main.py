from fastapi import FastAPI
from .api import routers

app = FastAPI(
    title="Internship Portal API",
    description="This is the Internship Portal API developed by Al-Khair Pama. It handles user management, job postings, and more.",
)


ROUTES = [("interns", "Interns"), ("companies", "Companies")]


for router, (name, tags) in zip(routers['v1'], ROUTES):
    app.include_router(router=router, prefix=f"/api/v1/{name}")


@app.get("/")
async def root():
    return {"message": "Hello, World!"}
