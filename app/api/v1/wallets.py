from app.models import User
from app.service import wallets
from app.scemas import OperationCreateWallet
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependency import get_db, get_current_user

router = APIRouter()

@router.get('/get_balance')
def get_balance(wallet_name: str | None = None, db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)):
    return wallets.get_balance(db, current_user, wallet_name=wallet_name)


@router.post('/create_wallet/{name}')
def create_wallet(wallet: OperationCreateWallet, db: Session = Depends(get_db),
                  current_user: User = Depends(get_current_user)):
    return wallets.create_wallet(db, current_user, wallet=wallet)