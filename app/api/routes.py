from fastapi import APIRouter, Depends
from app.schemas.auth import LoginRequest
from app.schemas.task import CreateTaskRequest
from app.services.auth_service import AuthService
from app.services.task_service import TaskService
from app.dependencies import get_auth_service, get_current_user, get_task_service

router = APIRouter()

@router.post("/login")
def login(
    data: LoginRequest,
    service: AuthService = Depends(get_auth_service)
):
    return service.login(data.name, data.password)

@router.get("/tasks")
def get_all_tasks(
    service: TaskService = Depends(get_task_service),
    user = Depends(get_current_user)
):
    return service.get_all()

@router.post("/tasks")
def create_task(
    data: CreateTaskRequest,
    service: TaskService = Depends(get_task_service),
    user = Depends(get_current_user)
):
    return service.create(data.description, int(user["sub"]))
