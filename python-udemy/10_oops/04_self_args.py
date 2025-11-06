class Shape:
  length = 1

  def display_length(self):
    print(f"Length is: {self.length}")

shape1 = Shape()
shape1.display_length()  # Accessing class attribute via instance method

print(Shape.display_length(shape1))