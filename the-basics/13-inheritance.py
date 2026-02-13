class Vehicle:
    def move(self):
        print("I am moving")


class Car(Vehicle):
    def honk(self):
        print("Honk! Honk!")


my_car = Car()
my_car.move()  # Output: I am moving
my_car.honk()  # Output: Honk! Honk!
