# vehicles.py

class Vehicle:
    def move(self):
        print("The vehicle moves forward.")

class Car(Vehicle):
    def move(self):
        print("🚗 The car drives on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ The plane flies in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚤 The boat sails across the water.")

# Main program
if __name__ == "__main__":
    # Create instances
    my_car = Car()
    my_plane = Plane()
    my_boat = Boat()

    # List of vehicles
    vehicles = [my_car, my_plane, my_boat]

    # Polymorphic behavior
    for v in vehicles:
        v.move()
