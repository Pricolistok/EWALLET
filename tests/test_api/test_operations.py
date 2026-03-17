from decimal import Decimal

from app.models import User, Wallet


def test_add_expense(db_session, client):
    ## Average
    user = User(login='test')
    db_session.add(user)
    db_session.flush()
    wallet = Wallet(name='card', balance=200, user_id=user.id)
    db_session.add(wallet)
    db_session.commit()
    db_session.refresh(wallet)

    response = client.post(
        "/api/v1/operation/expense",
        json={
            "wallet_name": "card",
            "amount": 50,
            "description": "Food"
        },
        headers={"Authorization": f'Bearer {user.login}'}
    )

    assert response.status_code == 200
    assert response.json()["message"] == f'Amount was added to card wallet'
    assert response.json()[f"balance wallet card"] == Decimal(150)


def test_add_negative_expense(db_session, client):
    ## Average
    user = User(login='test')
    db_session.add(user)
    db_session.flush()
    wallet = Wallet(name='card', balance=200, user_id=user.id)
    db_session.add(wallet)
    db_session.commit()
    db_session.refresh(wallet)

    response = client.post(
        "/api/v1/operation/expense",
        json={
            "wallet_name": "card",
            "amount": -50,
            "description": "Food"
        },
        headers={"Authorization": f'Bearer {user.login}'}
    )

    assert response.status_code == 422

def test_add_expense_to_empty_card(db_session, client):
    ## Average
    user = User(login='test')
    db_session.add(user)
    db_session.flush()
    wallet = Wallet(name='card', balance=200, user_id=user.id)
    db_session.add(wallet)
    db_session.commit()
    db_session.refresh(wallet)

    response = client.post(
        "/api/v1/operation/expense",
        json={
            "wallet_name": "  ",
            "amount": 50,
            "description": "Food"
        },
        headers={"Authorization": f'Bearer {user.login}'}
    )

    assert response.status_code == 422

def test_add_expense_to_not_found_card(db_session, client):
    ## Average
    user = User(login='test')
    db_session.add(user)
    db_session.flush()
    wallet = Wallet(name='card', balance=200, user_id=user.id)
    db_session.add(wallet)
    db_session.commit()
    db_session.refresh(wallet)

    response = client.post(
        "/api/v1/operation/expense",
        json={
            "wallet_name": "card1",
            "amount": 50,
            "description": "Food"
        },
        headers={"Authorization": f'Bearer {user.login}'}
    )

    assert response.status_code == 404


def test_add_expense_unauthorized(db_session, client):
    ## Average
    response = client.post(
        "/api/v1/operation/expense",
        json={
            "wallet_name": "card1",
            "amount": 50,
            "description": "Food"
        },
        headers={"Authorization": f'Bearer people'}
    )

    assert response.status_code == 401

def test_add_expense_more_money(db_session, client):
    ## Average
    user = User(login='test')
    db_session.add(user)
    db_session.flush()
    wallet = Wallet(name='card', balance=200, user_id=user.id)
    db_session.add(wallet)
    db_session.commit()
    db_session.refresh(wallet)

    response = client.post(
        "/api/v1/operation/expense",
        json={
            "wallet_name": "card",
            "amount": 1050,
            "description": "Food"
        },
        headers={"Authorization": f'Bearer {user.login}'}
    )

    assert response.status_code == 400
