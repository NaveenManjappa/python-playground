# Set {} = mutable(add/remove),unordered, NO duplicates, best for membership testing

fruits = {"Apple", "Orange", "Banana", "Mango"}

# fruits[0] = "Pineapple" # does not support item assignment
fruits.add("Mango")  # does not throw error but item gets added only once
# fruits.remove("coconut") # throws KeyError

fruits.pop()

# fruits.pop(0) # Type error: pop takes no arguments for sets

for fruit in fruits:
    print(fruit, end=" ")
print()

fruit = input("Enter a fruit to search for: ")

if fruit in fruits:
    print(f"{fruit} was found")
else:
    print(f"{fruit} was not found!")
