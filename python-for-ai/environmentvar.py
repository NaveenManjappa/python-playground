import os
from dotenv import load_dotenv

load_dotenv()

# Read from environment
api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_NAME", "default.db")

print(f"Using database: {api_key}")


def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total


shopping_cart = [
    {"name": "apple", "price": 0.5, "quantity": 6},
    {"name": "banana", "price": 0.3, "quantity": 8},
]
print(calculate_total(shopping_cart))
