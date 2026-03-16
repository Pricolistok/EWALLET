from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.dependency import get_current_user, get_db
from app.scemas import UserRequest, UserResponse
from app.models import User
from app.service.users import create_user as create_user_service

router = APIRouter()

@router.post('/users', response_model=UserResponse)
def create_user(payload: UserRequest, db: Session = Depends(get_db)):
    return create_user_service(db, payload.login)

@router.get("users/me", response_model=UserResponse)
def current_user(current_user: User = Depends(get_current_user)):
    return UserResponse.model_validate(current_user)

