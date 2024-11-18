# Type casting = the process of converting one variable from one data type to another
# str(), int(), float(), bool()
from sys import flags

name = "Adam Smith"
age = 36
gpa = 4.6
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = float(age)
print(age)

age = str(age)
# age += 1 # Get type error
age += "1"
print(age)
print(type(age))

name = bool(name)
print(name)

name2 = ""
print(bool(name2))