from cat import Cat

print("Welcome to my cat game!")

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
""")
    