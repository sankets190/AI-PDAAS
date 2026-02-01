# pyright: reportMissingImports=false

from fastapi import FastAPI
from app.core.database import engine
from app.models import user  # noqa: F401

app = FastAPI(title="AI-PDAAS")

@app.on_event("startup")
def startup():
    try:
        user.Base.metadata.create_all(bind=engine)
        print("✅ Database connected & tables created")
    except Exception as e:
        print("❌ Startup failed:", e)

@app.get("/")
def root():
    return {"status": "Backend + DB + User model ready"}
