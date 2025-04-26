# superhero.py

# Base class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def display_identity(self):
        print(f"🦸‍♂️ I am {self.name}, protector of {self.city}!")

    def use_power(self):
        print(f"⚡ {self.name} uses {self.power}!")

# Derived class (subclass)
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    # Polymorphism: override the use_power method
    def use_power(self):
        print(f"🛫 {self.name} soars through the skies at {self.flight_speed} km/h using {self.power}!")



# Main program
hero1 = Superhero("Night Guardian", "Invisibility", "Nairobi")
hero2 = FlyingSuperhero("Sky Dancer", "Wind Control", "Mombasa", 500)

hero1.display_identity()
hero1.use_power()

print("\n---\n")

hero2.display_identity()
hero2.use_power()
