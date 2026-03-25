from sqlalchemy.orm import Session
from app.models import Task

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Task).all()

    def create(self, data: dict):
        task = Task(**data)

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task
