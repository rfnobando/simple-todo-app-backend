from fastapi import FastAPI
from app.api.routes import router
from app.database import engine

app = FastAPI()

app.include_router(router)

@app.on_event("startup")
def startup():
    try:
        with engine.connect():
            print("Database Connection Test OK")
    except Exception as e:
        print("Database Connection Test failed:", e)
