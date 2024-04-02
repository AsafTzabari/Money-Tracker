from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
import httpx
from model import Transaction
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8001",
    "http://localhost:7000",
    "http://frontend:3000",
    "http://frontend:8001",
    "http://frontend:8000",
    "http://frontend:8080",
    "http://Frontend:3000",
    "http://Frontend:8001",
    "http://Frontend:8000",
    "http://Frontend:8080",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
mongodb_microservice_url = "http://asaf_mongocode:27000" 

@app.get("/")
async def get_all_documents():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{mongodb_microservice_url}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


@app.get("/get/{document_id}")
async def get_document(document_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{mongodb_microservice_url}/get/{document_id}")
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)


@app.get("/balance/")
async def calculate_balance():
    transactions = await get_all_documents()

    total_income = 0
    total_expenses = 0

    for transaction in transactions:
        if transaction["is_income"]:
            total_income += transaction["price"]
        else:
            total_expenses += transaction["price"]

    balance = total_income - total_expenses

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "balance": balance,
    }


@app.get("/chart_data/")
async def get_chart_data():
    transactions = await get_all_documents()

    expense_data = {}
    income_data = {}

    for transaction in transactions:
        category = transaction["category"]
        price = transaction["price"]
        is_income = transaction["is_income"]

        if is_income:
            income_data[category] = income_data.get(category, 0) + price
        else:
            expense_data[category] = expense_data.get(category, 0) + price

    chart_data = {
        "expense_data": expense_data,
        "income_data": income_data,
    }

    return chart_data


@app.post("/create/")
async def create_document(transaction: Transaction):
    async with httpx.AsyncClient() as client:
        transaction_data = dict(transaction)
        response = await client.post(
            f"{mongodb_microservice_url}/create/", json=transaction_data
        )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)


@app.put("/update/{id}")
async def update_document(id: str, transaction: Transaction):
    async with httpx.AsyncClient() as client:
        transaction_data = dict(transaction)
        response = await client.put(
            f"{mongodb_microservice_url}/update/{id}", json=transaction_data
        )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)


@app.delete("/delete/{document_id}")
async def delete_document(document_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"{mongodb_microservice_url}/delete/{document_id}"
        )
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)


