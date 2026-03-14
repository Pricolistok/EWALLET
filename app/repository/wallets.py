BALANCE: dict[str, float] = {}

def check_wallet_exist(wallet_name: str) -> bool:
    return wallet_name in BALANCE

def income_balance(name_wallet: str, amount: float) -> float:
    BALANCE[name_wallet] += amount
    return BALANCE[name_wallet]

def expense_balance(name_wallet: str, amount: float) -> float:
    BALANCE[name_wallet] -= amount
    return BALANCE[name_wallet]

def get_balance_repo(name_wallet: str) -> float:
    return BALANCE[name_wallet]

def get_total_balance():
    return sum(BALANCE.values())

def init_wallet(name_wallet: str, init_balance: float) -> None:
    BALANCE[name_wallet] = init_balance
