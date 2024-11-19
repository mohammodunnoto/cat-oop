class Device:
    def __init__(self, given_height, given_width, given_name):
        self.name = given_name
        self.height = given_height
        self.width = given_width
    def power_on(self):
        print("The device has turned on!")

class Computer(Device):
    def power_on(self):
        print(f"Your {self.name} has turned on!")
    def power_off(self):
        print(f"Your {self.name} has turned off!")
    def open_google(self):
        print("You have opened Google!")
    
dellprecisiontower3420 = Computer(29, 9.3, "Dell Precision Tower 3420")
dellprecisiontower3420.power_on()
dellprecisiontower3420.open_google()
dellprecisiontower3420.power_off()
