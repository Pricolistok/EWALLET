from app.service import operations as wallets_service
from fastapi import APIRouter
from app.scemas import OperationRequest

router = APIRouter()

@router.post('/operation/income')
def add_income(operation: OperationRequest):
    return wallets_service.add_income(operation)

@router.post('/operation/expense')
def add_expense(operation: OperationRequest):
    return wallets_service.add_expense(operation)
