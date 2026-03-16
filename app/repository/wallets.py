from decimal import Decimal
from typing import List
from sqlalchemy.orm import Session
from app.models import Wallet

def check_wallet_exist(db: Session, wallet_name: str) -> bool:
    return db.query(Wallet).filter(Wallet.name == wallet_name).first() is not None

def income_balance(db: Session, name_wallet: str, amount: Decimal) -> Wallet:
    wallet = db.query(Wallet).filter(Wallet.name == name_wallet).first()
    wallet.balance += amount
    return wallet


def expense_balance(db: Session, name_wallet: str, amount: Decimal) -> Wallet:
    wallet = db.query(Wallet).filter(Wallet.name == name_wallet).first()
    wallet.balance -= amount
    return wallet

def get_balance_repo(db: Session, name_wallet: str) -> Wallet:
    return db.query(Wallet).filter(Wallet.name == name_wallet).first()

def get_total_balance(db: Session) -> List[Wallet]:
    return db.query(Wallet).all()

def init_wallet(db: Session, name_wallet: str, init_balance: Decimal) -> Wallet:
    wallet = Wallet(name=name_wallet, balance=init_balance)
    db.add(wallet)
    return wallet
