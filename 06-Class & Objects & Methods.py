# Class & Objects & Methods
# Everything is an Object in Python
# OOP's has two concepts Attributes(Creating variable) and Behaviour (methods)

class Computer:  # defining a class

    def config(self):   # Here functions are called as methods because when it is declared under class
        print("i5, 16gb, 1TB")

com1 = Computer() #assiging a class to a object i.e, here com1 is a object 
com2 = Computer()


Computer.config(com1) # traditionl way of calling class by passing object ( Calling by order - Class,Method and Object)
Computer.config(com2)

com1.config() # mostly used one for calling class by passing object ( Calling by order - Object and Method)
com2.config()
