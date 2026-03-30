from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router
from app.database import engine

app = FastAPI()

origins = [
    "http://localhost:10002"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.on_event("startup")
def startup():
    try:
        with engine.connect():
            print("Database Connection Test OK")
    except Exception as e:
        print("Database Connection Test failed:", e)
