from typing import TypedDict, Annotated
import operator

# 1. ANNOTATED: Define a type with metadata
PositiveInt = Annotated[int, "Must be > 0"]

# 2. TYPEDDICT: Define a schema for a 'Product'
class Product(TypedDict):
    name: str
    price: PositiveInt

# 3. INHERITANCE: Create a specialized Product
class DiscountedProduct(Product):
    discount: float

# 4. GENERICS: A list of these specific dictionaries
cart: list[DiscountedProduct] = [
    {"name": "Laptop", "price": 1000, "discount": 0.1},
    {"name": "Mouse",  "price": 50,   "discount": 0.0}
]

# 5. FUNCTION REFERENCE & OPERATOR:
# A function that takes another function (strategy) to calculate values
def apply_operation(a, b, func_ref):
    return func_ref(a, b)

# Using operator.sub (subtraction) to calculate price difference
diff = apply_operation(1000, 50, operator.sub)
print(f"Difference: {diff}")