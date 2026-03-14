from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel


class OperationRequest(BaseModel):
    wallet_name: str
    amount: float
    description: str | None = None

app = FastAPI()
BALANCE = {}

@app.get('/test')
def test():
    return Response(status_code=200)


@app.get('/get_balance')
def get_balance(wallet_name: str | None = None):
    if wallet_name is None:
        return f'total ablance: {sum(BALANCE.values())}'

    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail=f'Wallet with name {wallet_name} not found'
        )
    return f'balance of wallet {wallet_name}: {BALANCE[wallet_name]}'


@app.post('/add_wallet/{name}')
def create_wallet(name: str, init_balance: float = 0):
    if name in BALANCE:
        raise HTTPException(status_code=400, detail=f'Wallet {name} already exists')
    BALANCE[name] = init_balance
    return {
        "message": f'Wallet "{name}" created',
        "wallet": name,
        "balance": init_balance
    }

@app.post('/operation/income')
def add_income(operation: OperationRequest):
    if operation.wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail='Wallet not found'
        )
    if operation.amount < 0:
        raise HTTPException(
            status_code=400,
            detail='Amount smaller zero'
        )
    BALANCE[operation.wallet_name] += operation.amount
    return {
        "message": f'Amount was added to {operation.wallet_name} wallet',
        f"balance wallet {operation.wallet_name}": BALANCE[operation.wallet_name]
    }

@app.post('/operation/expense')
def add_expense(operation: OperationRequest):
    if operation.wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail='Wallet not found'
        )
    if operation.amount < 0:
        raise HTTPException(
            status_code=400,
            detail='Amount smaller zero'
        )
    BALANCE[operation.wallet_name] -= operation.amount
    return {
        "message": f'Amount was added to {operation.wallet_name} wallet',
        f"balance wallet {operation.wallet_name}": BALANCE[operation.wallet_name]
    }



