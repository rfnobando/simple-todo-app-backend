from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.utils.auth import create_access_token, verify_password

class AuthService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def login(self, name: str, password: str):
        user = self.repo.get_by_name(name)

        if not user or not verify_password(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        
        token = create_access_token({"sub": str(user.id)})

        return {
            "message": "Login successful",
            "token": token
        }
