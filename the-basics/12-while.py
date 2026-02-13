# While loop = used to repeat a block of code as long as the condition remains True, we recheck the condition at the end of the loop

if 1 == 1:
    print("I am stuck in a loop!")

name = input("Enter your name: ")
print(name)

while name == "":
    name = input("Enter your name: ")

age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be less than zero")
    age = int(input("Enter your age: "))

print(f"Hello, {name}")
print(f"Your age is {age}")
