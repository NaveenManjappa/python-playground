class Shape:
    length = 1
    breadth = 1


shape1 = Shape()
print(
    f"Before shadowing: shape1.length = {shape1.length}, shape1.breadth = {shape1.breadth}"
)
shape1.length = (
    5  # This creates an instance attribute 'length' that shadows the class attribute
)
print(
    f"After shadowing: shape1.length = {shape1.length}, shape1.breadth = {shape1.breadth}"
)
print(f"Class attribute Shape.length = {Shape.length}, Shape.breadth = {Shape.breadth}")

del shape1.length  # Remove the instance attribute 'length'
print(
    f"After deleting instance attribute: shape1.length = {shape1.length}, shape1.breadth = {shape1.breadth}"
)

shape1.height = 10  # New instance attribute
print(f"Instance attribute shape1.height = {shape1.height}")
del shape1.height  # Remove the instance attribute 'height'
#print(f"Instance attribute shape1.height = {shape1.height}")  # This would raise an AttributeError