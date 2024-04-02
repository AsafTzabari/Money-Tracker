from pydantic import BaseModel

class Transaction(BaseModel):
    price: float
    category: str
    description: str
    is_income: bool
    date: str

 