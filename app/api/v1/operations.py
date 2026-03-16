from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.dependency import get_db, get_current_user
from app.models import User

from app.service import operations as wallets_service
from fastapi import APIRouter
from app.scemas import OperationRequest

router = APIRouter()

@router.post('/operation/income')
def add_income(operation: OperationRequest, db: Session = Depends(get_db),
               current_user: User = Depends(get_current_user)):
    return wallets_service.add_income(db, current_user, operation)

@router.post('/operation/expense')
def add_expense(operation: OperationRequest, db: Session = Depends(get_db),
                current_user: User = Depends(get_current_user)):
    return wallets_service.add_expense(db, current_user, operation)
