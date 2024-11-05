class Cat:
    # the constructor
    # the constructor will create a cat for us in code
    # to create a cat, we need given_name & given_colour
    # self is the cat that we are creating
    def __init__(self, given_name, given_colour):
        # name attribute
        self.name = given_name
        # colour attribute
        self.colour = given_colour
        self.age = 1
        self.energy = 50
        self.intelligence = 5
        self.weight = 5

    def train(self):
        print(f"{self.name} had a great time and learned a new trick!")
        self.energy -= 5
        self.intelligence += 1
        self.age += 0.1

    def feed(self):
        print(f"{self.name} has eaten a big meal!")
        self.energy += 10
        self.weight += 1
        self.age += 0.1

    def play(self):
        print(f"{self.name} is playing with you! It is having a lot of fun!")
        self.energy -= 5
        self.age += 0.1