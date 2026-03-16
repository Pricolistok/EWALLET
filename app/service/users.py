from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repository.users import create_user as create_user_repo, get_user
from app.scemas import UserResponse


def create_user(db: Session, login: str) -> UserResponse:
    if get_user(db, login):
        raise HTTPException(status_code=400, detail='User already exist')
    user = create_user_repo(db, login)
    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)