from datetime import datetime, timezone
from app.repositories.task_repository import TaskRepository


class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def get_all(self):
        return {"data": self.repo.get_all()}

    def create(self, description: str, user_id: int):
        new_task = {
            "description": description,
            "user_id": user_id,
            "created_at": datetime.now(timezone.utc)
        }

        return {"data": self.repo.create(new_task)}
