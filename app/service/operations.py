from fastapi import HTTPException

from app.scemas import OperationRequest
from app.repository.wallets import check_wallet_exist, income_balance, get_balance_repo, expense_balance
from app.database import Session

def add_income(db: Session, operation: OperationRequest):
    if not check_wallet_exist(db, wallet_name=operation.wallet_name):
        raise HTTPException(
            status_code=404,
            detail='Wallet not found'
        )
    wallet = income_balance(db, operation.wallet_name, operation.amount)
    db.commit()
    db.refresh(wallet)
    return {
        "message": f'Amount was added to {operation.wallet_name} wallet',
        f"balance wallet {operation.wallet_name}": wallet.balance
    }

def add_expense(db: Session, operation: OperationRequest):
    db = Session()
    try:
        if not check_wallet_exist(db, operation.wallet_name):
            raise HTTPException(
                status_code=404,
                detail='Wallet not found'
            )
        if operation.amount > get_balance_repo(db=db, name_wallet=operation.wallet_name).balance:
            raise HTTPException(
                status_code=400,
                detail='Insufficient funds'
            )
        wallet = expense_balance(db, name_wallet=operation.wallet_name, amount=operation.amount)
        db.commit()
        db.refresh(wallet)
        return {
            "message": f'Amount was added to {operation.wallet_name} wallet',
            f"balance wallet {operation.wallet_name}": wallet.balance
        }
    finally:
        db.close()