from typing import Generator

from app.database import Session as Session_db
from sqlalchemy.orm import Session


def get_db() -> Generator[Session, None, None]:
    db = Session_db()
    try:
        yield db
    finally:
        db.close()