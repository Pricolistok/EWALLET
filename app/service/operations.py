from fastapi import HTTPException

from app.scemas import OperationRequest
from app.repository.wallets import check_wallet_exist, income_balance, get_balance_repo, expense_balance

def add_income(operation: OperationRequest):
    if not check_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail='Wallet not found'
        )
    new_balance = income_balance(operation.wallet_name, operation.amount)
    return {
        "message": f'Amount was added to {operation.wallet_name} wallet',
        f"balance wallet {operation.wallet_name}": new_balance
    }

def add_expense(operation: OperationRequest):
    if not check_wallet_exist(operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail='Wallet not found'
        )
    if operation.amount > get_balance_repo(name_wallet=operation.wallet_name):
        raise HTTPException(
            status_code=400,
            detail='Insufficient funds'
        )
    new_balance = expense_balance(name_wallet=operation.wallet_name, amount=operation.amount)
    return {
        "message": f'Amount was added to {operation.wallet_name} wallet',
        f"balance wallet {operation.wallet_name}": new_balance
    }