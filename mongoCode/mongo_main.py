from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from model import Transaction
import mongoDbConnector

from schemas import list_serial, individual_serial
from bson import ObjectId

app = FastAPI()

origins = [
    "http://localhost:27000",
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


@app.get("/")
async def get_all_documents():
    documents = []
    con = mongoDbConnector.connect()

    Transactions = list_serial(con.find())

    return Transactions


@app.get("/get/{id}")
async def get_transaction(id: str):
    con = mongoDbConnector.connect()
    transaction = individual_serial(con.find_one({"_id": ObjectId(id)}))
    if transaction:
        return transaction
    else:
        raise HTTPException(status_code=404, detail="Transaction not found")


@app.post("/create/")
async def post_transactions(transaction: Transaction):
    con = mongoDbConnector.connect()
    con.insert_one(dict(transaction))
    return {"message": "Document created successfully"}


@app.put("/update/{id}")
async def put_transaction(id: str, transaction: Transaction):
    con = mongoDbConnector.connect()

    con.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(transaction)})
    return {"message": "Document updated successfully"}


@app.delete("/delete/{id}")
async def delete_document(id: str):
    con = mongoDbConnector.connect()
    individual_serial(con.find_one_and_delete({"_id": ObjectId(id)}))
    return {"message": "Document deleted successfully"}


@app.get("/insert_many/")
async def insert_many_for_test():
    con = mongoDbConnector.connect()
    examples = [
        {
            "price": 1234,
            "category": "Bonus",
            "description": "Year-end bonus",
            "is_income": True,
            "date": "2024-03-27",
        },
        {
            "price": 1500,
            "category": "Freelance",
            "description": "Graphic design project",
            "is_income": True,
            "date": "2024-03-23",
        },
        {
            "price": 500,
            "category": "Consulting",
            "description": "Consulting fee",
            "is_income": True,
            "date": "2024-03-20",
        },
        {
            "price": 600,
            "category": "Part-time",
            "description": "Part-time job payment",
            "is_income": True,
            "date": "2024-03-15",
        },
        {
            "price": 2000,
            "category": "Overtime",
            "description": "Overtime payment",
            "is_income": True,
            "date": "2024-03-11",
        },
        {
            "price": 50,
            "category": "Groceries",
            "description": "Weekly grocery shopping",
            "is_income": False,
            "date": "2024-03-26",
        },
        {
            "price": 200,
            "category": "Utilities",
            "description": "Electricity bill",
            "is_income": False,
            "date": "2024-03-25",
        },
        {
            "price": 300,
            "category": "Rent",
            "description": "Monthly rent",
            "is_income": False,
            "date": "2024-03-24",
        },
        {
            "price": 40,
            "category": "Transportation",
            "description": "Bus fare",
            "is_income": False,
            "date": "2024-03-22",
        },
        {
            "price": 100,
            "category": "Entertainment",
            "description": "Concert tickets",
            "is_income": False,
            "date": "2024-03-21",
        },
    ]
    con.insert_many(examples)
    return {"message": "Documents inserted successfully"}
