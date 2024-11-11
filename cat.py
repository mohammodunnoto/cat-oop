import os
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
        os.system("clear")
        print(f""""{self.name} had a great time and learned a new trick!
 _._     _,-'""`-._
(,-.`._,'(       |\`-/|
    `-.-' \ )-`( , o o)
          `-    \`_`"'-
              """)
        self.energy -= 5
        self.intelligence += 1
        self.age += 0.1

    def feed(self):
        os.system("clear")
        print(f"""{self.name} has eaten a big meal!
    |\__/,|   (`\
  _.|o o  |_   ) )
-(((---(((--------
              """)
        self.energy += 10
        self.weight += 1
        self.age += 0.1

    def play(self):
        os.system("clear")
        print(f"""{self.name} is playing with you! It is having a lot of fun!
("`-''-/").___..--''"`-._ 
 `6_ 6  )   `-.  (     ).`-.__.`) 
 (_Y_.)'  ._   )  `._ `. ``-..-' 
   _..`--'_..-_/  /--'_.'
  ((((.-''  ((((.'  (((.-' 
              """)
        self.energy -= 5
        self.age += 0.1

    def sleep(self):
        os.system("clear")
        print(f"""{self.name} is having a nap.
      |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
     |,4-  ) )-,_. ,\ (  `'-'
    '---''(_/--'  `-'\_)
              """)
        self.energy += 20
        self.age += 0.1

    def stats(self):
        os.system("clear")
        print(f"""These are {self.name}'s stats.
    Age: {self.age}
    Energy: {self.energy}
    Intelligence: {self.intelligence}
    Weight: {self.weight}
  ^~^  ,
 ('Y') )
 /   \/ 
(\|||/) 
""")