from fastapi import HTTPException

from app.models import User
from app.scemas import OperationRequest
from app.repository.wallets import check_wallet_exist, income_balance, get_balance_repo, expense_balance
from app.database import Session

def add_income(db: Session, current_user: User, operation: OperationRequest):
    if not check_wallet_exist(db, current_user.id, wallet_name=operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail='Wallet not found'
        )
    wallet = income_balance(db, current_user.id, operation.wallet_name, operation.amount)
    db.commit()
    db.refresh(wallet)
    return {
        "message": f'Amount was added to {operation.wallet_name} wallet',
        f"balance wallet {operation.wallet_name}": wallet.balance
    }

def add_expense(db: Session, current_user: User, operation: OperationRequest):
    if not check_wallet_exist(db, current_user.id, operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail='Wallet not found'
        )
    if operation.amount > get_balance_repo(db=db, user_id=current_user.id, name_wallet=operation.wallet_name).balance:
        raise HTTPException(
            status_code=400,
            detail='Insufficient funds'
        )
    wallet = expense_balance(db, current_user.id, name_wallet=operation.wallet_name, amount=operation.amount)
    db.commit()
    db.refresh(wallet)
    return {
        "message": f'Amount was added to {operation.wallet_name} wallet',
        f"balance wallet {operation.wallet_name}": wallet.balance
    }