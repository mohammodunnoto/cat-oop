from cat import Cat
from pyfiglet import Figlet
import os
os.system("clear")
j = Figlet(font='doom')
print(j.renderText("Welcome to my cat game!"))

name = input("Enter a name for your cat:\n")
colour = input("Enter a colour for your cat:\n")
my_cat = Cat(name,colour)

while True:
    action = input("""
What would you like to do with your cat?
1. Train
2. Feed
3. Play
4. Sleep
5. Show stats\n
""")

    if action == "1":
        my_cat.train()
    elif action == "2":
        my_cat.feed()
    elif action == "3":
        my_cat.play()
    elif action == "4":
        my_cat.sleep()
    elif action == "5":
        my_cat.stats()