# 1. Basic Variable Hinting
# We explicitly state that 'player_name' is a string and 'level' is an integer
player_name: str = "Mario"
level: int = 5


# 2. Function Type Hinting
# Arguments 'a' and 'b' are floats, and the function returns a float
def calculate_area(width: float, height: float) -> float:
    return width * height


# 3. Generics (Lists)
# A list that can ONLY contain strings
inventory: list[str] = ["Sword", "Shield", "Potion"]

# 4. Generics (Dictionaries)
# A dictionary where keys are strings (items) and values are integers (quantities)
item_counts: dict[str, int] = {"Sword": 1, "Potion": 5}

# A coordinate pair (x, y)
point: tuple[int, int] = (10, 20)

# ---------------------------------------------------------
# If you run this code, Python is happy.
# If you tried: inventory.append(100)  <-- Your editor would warn you!
# ---------------------------------------------------------

inventory.append(
    100
)  # This will cause a type checker to raise an error, as 100 is not a string.
item_counts["Shield"] = (
    "Two"  # This will also raise an error, as the value should be an integer, not a string.
)
