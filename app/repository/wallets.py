from decimal import Decimal
from typing import List
from sqlalchemy.orm import Session
from app.models import Wallet

def check_wallet_exist(db: Session, user_id: int, wallet_name: str) -> bool:
    return db.query(Wallet).filter(Wallet.user_id == user_id).filter(Wallet.name == wallet_name).first() is not None

def income_balance(db: Session, user_id: int, name_wallet: str, amount: Decimal) -> Wallet:
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).filter(Wallet.name == name_wallet).first()
    wallet.balance += amount
    return wallet


def expense_balance(db: Session, user_id: int, name_wallet: str, amount: Decimal) -> Wallet:
    wallet = db.query(Wallet).filter(Wallet.user_id == user_id).filter(Wallet.name == name_wallet).first()
    wallet.balance -= amount
    return wallet

def get_balance_repo(db: Session, user_id: int, name_wallet: str) -> Wallet:
    return db.query(Wallet).filter(Wallet.user_id == user_id).filter(Wallet.name == name_wallet).first()

def get_total_balance(db: Session, user_id: int) -> List[Wallet]:
    return db.query(Wallet).filter(Wallet.user_id == user_id).all()

def init_wallet(db: Session, user_id: int, name_wallet: str, init_balance: Decimal) -> Wallet:
    wallet = Wallet(name=name_wallet, balance=init_balance, user_id=user_id)
    db.add(wallet)
    return wallet
