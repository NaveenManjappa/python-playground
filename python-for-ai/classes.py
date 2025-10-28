class Dog:
  def __init__(self, name,breed):
    self.name = name
    self.breed = breed

class Cat:
  def __init__(self, name, color):
    self.name = name
    self.color = color

jerry = Dog("Jerry","Labrador")
print(jerry.breed)