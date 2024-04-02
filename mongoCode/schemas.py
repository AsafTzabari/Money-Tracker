def individual_serial(transaction) -> dict:
    return {
        "id": str(transaction["_id"]),
        "price": transaction["price"],
        "category": transaction["category"],
        "description": transaction["description"],
        "is_income": transaction["is_income"],
        "date": transaction["date"],
    }


def list_serial(transactions) -> list:
    return [individual_serial(transaction) for transaction in transactions]
