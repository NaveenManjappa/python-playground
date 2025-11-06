class Shape:
    def __init__(self, length):
        self.length = length

    def display_length(self):
        print(f"Length is: {self.length}")


shape1 = Shape(2)
print(f"shape1.length = {shape1.length}")
shape1.display_length()
