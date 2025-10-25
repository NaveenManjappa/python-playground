name = "Alice" # valid variable name
age = 25

name = "Bob"

is_student = True

# 2age = 30 #invalid variable name as it cannot start with a number
# new-age = 35 #invalid variable name as it cannot contain hyphen

"""
This is a multi-line
string that can be used as a comment
"""

5 + 5

5 ** 2

my_long_string = """ 
This is a long string
that spans multiple lines.
My favorite quote is:
"To be, or not to be, that is the question.
"""

print(my_long_string)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

long_dash = "-" * 15
print(full_name)
print(long_dash)

len(full_name)

is_logged_in = False
is_admin = True
has_premium_account = False

age = 18
can_vote = age >= 18
print(can_vote)

age = 25
has_license = True
drunk = True

can_drive = age >=18 and has_license and not drunk
print(can_drive)

name = "Alice"
greeting = f"Hi there! My name is {name}!"
print(greeting)

text = "Python programming"
text.lower()
text.upper()
text.replace("Python", "JavaScript")
text.title()
print(text.replace("Python", "JavaScript"))

user_name = "user123"
password = "pass456"
is_valid_login = user_name == "user123" and password == "pass456"

if is_valid_login:
    print("Login successful!")
else:
    print("Invalid username or password.")


for i in range(5):
    i+=10
    print(i)

#Lists
#Lists are ordered, mutable, and allow duplicate elements.
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("date")
fruits.append("banana")
print(fruits)
fruits.remove("banana")
print(fruits)

print("Add date and remove banana",fruits)
print("First element",fruits[0])  # Accessing first element
print("Last element",fruits[-1]) # Accessing last element
print("Length",len(fruits)) # Length of the list
for fruit in fruits:
    print(fruit)
print(fruits[0:2])
print(fruits[::-1])  # Reversing the list
print("Is 'apple' in fruits?", "apple" in fruits)
print("Is 'banana' not in fruits?", "banana" not in fruits)
print("Fruits sorted:", sorted(fruits))  # Sorted list without modifying original
fruits.sort()  # Sorting the original list
print("Fruits after sort():", fruits)

fruits.insert(1, "blueberry")  # Inserting at index 1
print("After inserting blueberry at index 1:", fruits)

numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()
print("Sorted numbers:", numbers)
mixed_list = [1, "two", 3.0, True]
print("Mixed list:", mixed_list)
nested_list = [[1, 2, 3], ["a", "b", "c"]]
print("Nested list:", nested_list)
print("First element of nested list:", nested_list[0][0])  # Accessing element in nested list
empty_list = []
print("Empty list:", empty_list) 

#Dictionaries
#Dictionaries are unordered, mutable, and indexed by keys.
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person)
person["age"] = 31
print("Updated age:", person["age"])
person["profession"] = "Engineer"
print("Added profession:", person)
print("Keys:", person.keys())
print("Values:", person.values())
del person["city"]
print("After deleting city:", person)
print("Is 'name' a key in person?", "name1" in person)
for key, value in person.items():
    print(f"{key}: {value}")

#Tuples
#Tuples are ordered, immutable, and allow duplicate elements.
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)
print("First element:", coordinates[0])
print("Length:", len(coordinates))
# coordinates[0] = 15.0  # This will raise an error since tuples are immutable
print("Is 10.0 in coordinates?", 10.0 in coordinates)
print("Is 30.0 not in coordinates?", 30.0 not in coordinates)
print("Slicing", coordinates[0:1])
print("Reversed tuple:", coordinates[::-1])
print("Last element:", coordinates[-1])
#Tuples can contain mixed data types
mixed_tuple = (1, "two", 3.0, True)
print("Mixed tuple:", mixed_tuple)
#Nested tuples
nested_tuple = ((1, 2), ("a", "b"))
print("Nested tuple:", nested_tuple)
print("First element of nested tuple:", nested_tuple[0][0])  # Accessing
#Single-element tuple (note the comma)
single_element_tuple = (42,)
print("Single-element tuple:", single_element_tuple)
#Tuple unpacking
x,y = coordinates
print("Unpacked coordinates:", x,y)

#Sets
#Sets are unordered, mutable, and do not allow duplicate elements.
colors = {"red", "green", "blue"}
print("Colors set:", colors)
colors.add("yellow")
print("After adding yellow:", colors)
colors.remove("green")
print("After removing green:", colors)
print("Is 'red' in colors?", "red" in colors)
print("Is 'purple' not in colors?", "purple" not in colors)
colors.add("red")  # Adding duplicate has no effect
print("After adding duplicate red:", colors)
# Set operations
A = {1, 2, 3}
B = {3, 4, 5}
print("Union A|B:", A | B)
print("Intersection A&B:", A & B)
print("Difference A-B:", A - B)
 #list to sets 
L = [3, 1, 2, 3, 2]
print("Original list L:", L)
print("Type of L:", type(L))
S = set(L)
print("Converted to set S (unique elements):", S)






