from fastapi.params import Depends
from sqlalchemy.orm import Session
from app.dependency import get_db

from app.service import operations as wallets_service
from fastapi import APIRouter
from app.scemas import OperationRequest

router = APIRouter()

@router.post('/operation/income')
def add_income(operation: OperationRequest, db: Session = Depends(get_db)):
    return wallets_service.add_income(db, operation)

@router.post('/operation/expense')
def add_expense(operation: OperationRequest, db: Session = Depends(get_db)):
    return wallets_service.add_expense(db, operation)
