import pytest
from httpx import AsyncClient
from main import app


@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client

@pytest.mark.asyncio
async def test_create_transaction(client):
    transaction_data = {
        "price": 100,
        "category": "Food",
        "description": "Groceries",
        "is_income": False,
        "date": "2024-04-01",
    }
    response = await client.post("/create/", json=transaction_data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_transaction_bad_request(client):
    transaction_data = {
        "price": 100,
    }
    response = await client.post("/create/", json=transaction_data)
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_update_transaction(client):
    transaction_data = {
        "price": 100,
        "category": "Food",
        "description": "Groceries",
        "is_income": False,
        "date": "2024-04-01",
    }
    create_response = await client.post("/create/", json=transaction_data)
    assert create_response.status_code == 200
    transaction_id = create_response.json()["id"]

    update_data = {
        "price": 150,
        "category": "Food",
        "description": "Groceries",
        "is_income": False,
        "date": "2024-04-01",
    }
    response = await client.put(f"/update/{transaction_id}", json=update_data)
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_update_transaction_not_found(client):
    update_data = {
        "price": 150,
        "category": "Food",
        "description": "Groceries",
        "is_income": False,
        "date": "2024-04-01",
    }
    response = await client.put("/update/non_existent_id", json=update_data)
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_delete_transaction(client):
    transaction_data = {
        "price": 100,
        "category": "Food",
        "description": "Groceries",
        "is_income": False,
        "date": "2024-04-01",
    }
    create_response = await client.post("/create/", json=transaction_data)
    assert create_response.status_code == 200
    transaction_id = create_response.json()["id"]

    response = await client.delete(f"/delete/{transaction_id}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_transaction_not_found(client):
    response = await client.delete("/delete/non_existent_id")
    assert response.status_code == 404

@pytest.mark.asyncio
async def test_get_transactions(client):
    response = await client.get("/transactions/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_transaction_by_id(client):
    transaction_data = {
        "price": 100,
        "category": "Food",
        "description": "Groceries",
        "is_income": False,
        "date": "2024-04-01",
    }
    create_response = await client.post("/create/", json=transaction_data)
    assert create_response.status_code == 200
    transaction_id = create_response.json()["id"]

    response = await client.get(f"/get/{transaction_id}")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_transaction_by_id_not_found(client):
    response = await client.get("/get/non_existent_id")
    assert response.status_code == 404


@pytest.mark.asyncio
async def test_invalid_request(client):
    response = await client.put("/transactions/")
    assert response.status_code == 405
