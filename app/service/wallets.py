from fastapi import HTTPException
from app.scemas import OperationCreateWallet
from app.repository.wallets import check_wallet_exist, get_total_balance, get_balance_repo, init_wallet


def get_balance(wallet_name: str | None = None):
    if wallet_name is None:
        return f'total ablance: {get_total_balance()}'
    if not check_wallet_exist(wallet_name=wallet_name):
        raise HTTPException(
            status_code=404,
            detail=f'Wallet with name {wallet_name} not found'
        )
    return f'balance of wallet {wallet_name}: {get_balance_repo(name_wallet=wallet_name)}'


def create_wallet(wallet: OperationCreateWallet):
    if check_wallet_exist(wallet.wallet_name):
        raise HTTPException(status_code=400, detail=f'Wallet {wallet.wallet_name} already exists')
    init_wallet(wallet.wallet_name, wallet.init_balance)
    return {
        "message": f'Wallet "{wallet.wallet_name}" created',
        "wallet": wallet.wallet_name,
        "balance": wallet.init_balance
    }
