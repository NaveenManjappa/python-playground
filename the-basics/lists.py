# List [] = mutable, most flexible
# Tuple () = immutable, faster
# Set {} = mutable(add/remove),unordered, NO duplicates, best for membership testing

fruit = "Apple" # single variable

fruits = ["Apple", "Orange", "Banana", "Coconut"]
#list - collection of values

print(fruits)
print(fruits[2])

# fruits[3] = "Pineapple" #mutable
# fruits.append("Mango") #add or append to the list
# fruits.remove("Banana")

fruits.pop(3)

for fruit in fruits:
    print(fruit,end=" ")

fruits.clear()
