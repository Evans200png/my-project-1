# main class: Vehicle
class Vehicle:
    def move(self):
        pass  # Placeholder method for polymorphism

# sub class: Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road!")

# sub class: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky!")

# sub class: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing on the water!")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()  # Calls the overridden move() method based on the object type
