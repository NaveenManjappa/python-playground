def greet():
  print("Hello, Good Morning!")
  

greet() #calling the function

def check_weather(temp):
  if temp > 30:
    print("It's a hot day")
  else:
    print("It's a cool day")

check_weather(25)

def greet(name):
  print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

#function for simple interest
def simple_interest(principal, rate, time):
  interest = (principal * rate * time) / 100
  return interest
si = simple_interest(1000, 5, 3)
print(f"Simple Interest: {si}")

def greet_full_name(first_name="Naveen", last_name="Manjappa"):
  print(f"Hello, {first_name} {last_name}!")

greet_full_name("John", "Doe")
greet_full_name(last_name="Smith", first_name="Jane")
greet_full_name()  # uses default values

#Global and Local Variables
message = "Hello, World!"  # global variable
def greet():
  message = "Hello from inside the function!"  # local variable
  print(message)

greet()  # prints local variable
print(message)  # prints global variable

def add(a, b):
  return a + b

result = add(5, 3)
print(f"Addition Result: {result}")

def calculate_area(width, height):
  area = width * height
  return area

rect_area = calculate_area(5, 10)
print(f"Rectangle Area: {rect_area}")

def simple_function():
  numers = [1, 2, 3, 4, 5]
  first_num = numers[0]
  last_num = numers[-1]
  return first_num, last_num

first, last = simple_function()
print(f"First Number: {first}, Last Number: {last}")







