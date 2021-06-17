
# __init__ Method ( For Creating the variables inside the class )(also known as Constructer)

class Computer:

    def __init__(self,cpu,ram): # for Creating the variables(arguments)... (it is called automatically once when every time the class is called)
        self.cpu = cpu # assinging the variables to class by self (self is an object)
        self.ram = ram

    def config(self):
        print("Config is ",self.cpu, self.ram) # Self is used call the values further because it is used inside class ( it not a local variable)

com1 = Computer('i5',16) #passing the arguments
com2 = Computer('Ryzen 3',8)


com1.config() # calling the class
com2.config()

# Types of Variables in Class
# Using Instance Variable  and Class or (Static) Variable

class Car:

    wheels = 4  # Declaring variables inside the class are known as class or static variables when this value is changed it affects the entire class similar to global variable

    def __init__(self):  # Instance variables it is called every time when the function is called and creates a new heap memory
        self.mil = 10
        self.com = "BMW"


c1 = Car() 
c2 = Car()

c1.mil = 8

Car.wheels = 5  # changing static variable

print(c1.com , c1.mil , c1.wheels)
print(c2.com , c2.mil , c2.wheels)
