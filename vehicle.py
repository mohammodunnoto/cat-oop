class Vehicle:
    def __init__(self, given_name, given_speed, given_size):
        self.name = given_name
        self.speed = given_speed
        self.size = given_size
    def switch_on(self):
        print("You switched the vehicle on!")
    def drive(self):
        print("Your drove the vehicle!")
    def fix(self):
        print("You fixed the vehicle!")
    
class Car(Vehicle):
    def switch_on(self):
        print(f"You switched the {self.name} car on!")
    def drive(self):
        print(f"Your drove the {self.name}!")
    def fix(self):
        print(f"You fixed the {self.name}!")
    def drift(self):
        print(f"You attempted drifting the {self.name} but you crashed.")

class Motorbike(Vehicle):
    def switch_on(self):
        print(f"You switched the {self.name} motorbike on!")
    def drive(self):
        print(f"Your drove the {self.name}!")
    def fix(self):
        print(f"You fixed the {self.name}!")
    def wheelie(self):
        print(f"You attempted a wheelie on your {self.name} motorbike! You crashed.")

micra = Car("Nissan Micra", "112mph", "1.455m")
motorbike = Motorbike("Motorbike", "70mph", "0.7m")
micra.drive()
micra.drift()
micra.fix()
motorbike.drive()
motorbike.wheelie()
motorbike.fix()