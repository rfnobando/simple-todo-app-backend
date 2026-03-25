from fastapi import APIRouter, Depends
from app.schemas.auth import LoginRequest
from app.services.auth_service import AuthService
from app.dependencies import get_auth_service, get_current_user

router = APIRouter()

@router.get("/")
def root(user=Depends(get_current_user)):
    return {"message": "Hello World"}

@router.post("/login")
def login(data: LoginRequest, service: AuthService = Depends(get_auth_service)):
    return service.login(data.name, data.password)
