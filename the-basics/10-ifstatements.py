# if statements = execute some code only if a condition is True
# they allow for basic decision making - if, elif, else

age = int(input("Enter your age: "))
has_ticket = False
price = 10.00

if age >= 65:
    print("You are a senior citizen!")
    print(f"The ticket price for a senior citizen is £{price * 0.5}")
elif age >= 18:
    print("You are an adult")
    print(f"The ticket for price for an adult is £{price}")
elif age < 0:
    print("You have not  been born yet!")
elif age == 0:
    print("You were just born!")
else:
    print("You are a child")
    print(f"The ticket price for a child is £{price * 0.5}")

if has_ticket:
    print("You may enter. You have a ticket")
else:
    print("You need to buy a ticket")
