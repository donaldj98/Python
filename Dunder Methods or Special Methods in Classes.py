# __init__ method (Similar To constructor Method)
# This method is automatically called when the method is created (hello1 = hello()) 
# This acts like a mian function so whenever we create a class declare all the attributes to the init method 
# which helps in allocating the memory for the attributes which is needed for initilaizing the program
class add(self):
  def __init__(self):
    self.a=0
    self.b=0
    self.sum=0
  def sum(self):
    self.sum= self.a +self.b
addition=add() 

# __del__ object (destructer)
# after creating the object it help to delete the object which is created to free up the memory
def __del__(self):
  print("Object is deleted")
addition=add() 
del addition

# __str__ method (to view the object directly)
print(addition) # It only prints that its a main object
# if str is declared inside the class then return what is inside the class which is declared

class add(self):
  def sum_of(self):
    print(f'sum of {self.a} and {self.b} is {self.sum}')
  def __str__(self):
    print("I am in str method")
    return f'sum of {self.a} and {self.b} is {self.sum}' 
  #if i call both in same class then __str will be prioritized to call __repr__method then print(repr(addition))
  def __repr__(self):
    return f'sum of {self.a} and {self.b} is {self.sum}'  #both are same method but repr is official representation but __str__ is is informal
addition=add() 
print(addition) #its returns what is declared in the __str__ block

# __doc__ Method (it helps to print the doct=mentation ofr infor privided inside the class
class add(self):
  ''' Hello the class can add two numbers ''' # to priint this doc or info
addition=add() 
print(addition.__doc__) #prints the doc
  

