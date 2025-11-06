class Shape:
  length = 0
  

print(Shape.length)

Shape.breadth = 1
print(Shape.breadth)

shape1 = Shape()
print(f"Class length value {shape1.length}")
print(f"Class breadth value {shape1.breadth}")
shape1.length = 5

shape1.height = 10
print(shape1.height)
print(shape1.length)
