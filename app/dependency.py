from typing import Generator

from fastapi import HTTPException
from fastapi.params import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.database import Session as Session_db
from sqlalchemy.orm import Session
from app.repository.users import get_user as get_user_repo

from app.models import User

security = HTTPBearer()

def get_db() -> Generator[Session, None, None]:
    db = Session_db()
    try:
        yield db
    finally:
        db.close()

def get_current_user(credentionals: HTTPAuthorizationCredentials = Depends(security),
                     db: Session = Depends(get_db)) -> User:
    login = credentionals.credentials
    user = get_user_repo(db, login)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return user