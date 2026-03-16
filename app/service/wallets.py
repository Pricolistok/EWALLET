from fastapi import HTTPException
from app.scemas import OperationCreateWallet
from app.repository.wallets import check_wallet_exist, get_total_balance, get_balance_repo, init_wallet
from app.database import Session


def get_balance(db: Session, wallet_name: str | None = None):
    if wallet_name is None:
        return f'total ablance: {sum([i.balance for i in get_total_balance(db)])}'
    if not check_wallet_exist(db, wallet_name=wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f'Wallet with name {wallet_name} not found'
        )
    return f'balance of wallet {wallet_name}: {float(get_balance_repo(db, name_wallet=wallet_name).balance)}'

def create_wallet(db: Session, wallet: OperationCreateWallet):
    if check_wallet_exist(db, wallet.wallet_name):
        raise HTTPException(status_code=400, detail=f'Wallet {wallet.wallet_name} already exists')
    creator_wallet = init_wallet(db, wallet.wallet_name, wallet.init_balance)
    db.commit()
    db.refresh(creator_wallet)
    return {
        "message": f'Wallet "{creator_wallet.name}" created',
        "wallet": creator_wallet.name,
        "balance": creator_wallet.balance
    }
