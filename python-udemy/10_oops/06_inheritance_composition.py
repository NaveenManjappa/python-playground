class Shape:
  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth

class Rectangle(Shape):
  def area(self):
    return self.length * self.breadth
  
class Square:
  shapes = Shape

  def __init__(self):
    self.shape = self.shapes(0, 0)

  def area(self):
    return self.shape.length * self.shape.breadth 

rect1 = Rectangle(5, 3)
print(f"Rectangle area: {rect1.area()}")

