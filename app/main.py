from fastapi import FastAPI

app = FastAPI(title="AI-PDAAS")

@app.get("/")
def root():
    return {"status": "Backend running"}
