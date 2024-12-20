class Animal:
    def __init__(self, given_name, given_colour):
        self.name = given_name
        self.colour = given_colour
        self.age = 1
        self.energy = 100

    def make_noise(self):
        print("Animal made a noise!")

class Cat(Animal):
    def make_noise(self):
        print("Meow!")
    def scratch(self):
        print(f"{self.name} scratched you!")


sid = Cat('Sid', 'Black')
sid.make_noise()
sid.scratch()
