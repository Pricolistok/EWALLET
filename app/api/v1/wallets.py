from app.service import wallets
from app.scemas import OperationCreateWallet
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependency import get_db

router = APIRouter()

@router.get('/get_balance')
def get_balance(wallet_name: str | None = None, db: Session = Depends(get_db)):
    return wallets.get_balance(db, wallet_name=wallet_name)


@router.post('/create_wallet/{name}')
def create_wallet(wallet: OperationCreateWallet, db: Session = Depends(get_db)):
    return wallets.create_wallet(db, wallet=wallet)