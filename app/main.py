# pyright: reportMissingImports=false

from fastapi import FastAPI
from app.core.database import engine

app = FastAPI(title="AI-PDAAS")

@app.on_event("startup")
def startup():
    try:
        engine.connect()
        print("✅ Database connected successfully")
    except Exception as e:
        print("❌ Database connection failed:", e)

@app.get("/")
def root():
    return {"status": "Backend + Database connected"}
