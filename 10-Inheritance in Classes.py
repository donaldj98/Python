# Inheritance in Classes (one class under other) - Similar to Parent Child Relation

class A:                                #  A is Super class or Parent Class
    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")

class B:                                # B is sub class or Child class
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")
        
class B(A):                              # A class with B class Inherited (Single Level Inheritance)
    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(A,B):                           # C class with both A and B  (Multiple Inheritance)
    def feature5(self):
        print("Feature 5 working")


a1 = A()

a1.feature1()
a1.feature2()

b1 = B()

c1 = C()


# Single level Inheritance 
Class A       # Parent
Class B(A)    # Child Has acess of parent


# Multi Level Inheritance 
Class A       # grand parent
Class B(A)    # Parent
Class C(B)    # Child Has acess of both grand parent and parent

# Multiple Inheritance
Class A       # NO relation
Class B       # No relation
Class C(A,B)  # Has all acess of both A and B






