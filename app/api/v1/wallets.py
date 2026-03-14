from app.service import wallets
from app.scemas import OperationCreateWallet
from fastapi import APIRouter

router = APIRouter()

@router.get('/get_balance')
def get_balance(wallet_name: str | None = None):
    return wallets.get_balance(wallet_name=wallet_name)


@router.post('/create_wallet/{name}')
def create_wallet(wallet: OperationCreateWallet):
    return wallets.create_wallet(wallet=wallet)