import os
class Employee:
    def __init__(self, name, role, salary, DOB):
        self.name = name
        self.role = role
        self.salary = salary
        self.dob = DOB
    
    def increase_salary(self):
        os.system("clear")
        increase = int(input("How much would you like to increase the salary by?"))
        self.salary += increase
        print(f"The new salary is: {self.salary}")
    
    def calculate_age(self):
        os.system("clear")
        age = 2024 - self.dob
        print(f"The employee age is: {age}")

class Manager:
    def __init__(self, name, role, salary, DOB, bonus):
        self.name = name
        self.role = role
        self.salary = salary
        self.dob = DOB
        self.bonus = bonus
    
    def increase_salary(self):
        os.system("clear")
        sincrease = int(input("How much would you like to increase the salary by?"))
        self.salary += sincrease
        print(f"The new salary is: {self.salary}")
    
    def calculate_age(self):
        os.system("clear")
        age = 2024 - self.dob
        print(f"The manager's age is: {age}")
    
    def increase_salary(self):
        os.system("clear")
        bincrease = int(input("How much would you like to increase the bonus by?"))
        self.bonus += bincrease
        print(f"The new salary is: {self.bonus}")