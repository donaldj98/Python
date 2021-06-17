# types of method in a class
# 1-Instance Method - It is an Instant varibale which is used in declaring variables inside a class method used to perform certain tasks in it
# 2-Class Method  - It is an Class or Static(global)  which is declared inside a class to perform certain operations inside the class
# 3-Static Method - It is used to perform some opertions other than the class

class Student:

    school = 'Telusko' # Declaration of Static or class Variable

    def __init__(self,m1,m2,m3): # Decalration of Instance Variable
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # Finding average of intance variables - this is an instance method because we are using self to call and acess 
        return (self.m1 + self.m2 + self.m3)/3  

    @classmethod              # Type of a decorator used to denote class method (it avoids the passing of object )
    def getSchool(cls):       # Acessing the static or class variable by passing cls 
        return cls.school

    @staticmethod             # Type of a decorator used to denote static method (to avoid passing of the object while calling
    def info():               # keep it empty 
        print("This is Student class.. in abc molude") 

    # def get_m1(self):   # Getters just get the values (Acessors) - just accessing the value Instance Methods by passing self
    #     return self.m1
    #
    # def set_m1(self,value):  # Seters just sets the value (Mutators) - just assiging the values Instance method by passing self
    #     self.m1 = value

s1 = Student(34,47,32)
s2 = Student(89,32,12)



print(s1.avg()) # Printing instance method
print(Student.getSchool()) # printing class method

Student.info() # printing Static method
