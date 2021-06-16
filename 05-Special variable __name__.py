# Special variable __name__ 
# Points to remember ( It can be used in large projects where self created module has to be used again and again for further session / Reusage of code)
# __name__ variable acts as __main__ in current wrok area
# __name__ variable acts as module name when we are importing it in other workplaces 
# main function is starting function  which is exceuted in the beginning of code (Initaites the project or Starting point of the project)

calc.py (Created Module)

#print("calc says : ",__name__)

def add(a,b):
    c=a+b
    print("Result is : ",c)

def sub(a,b):
    c=a-b
    print("Result is : ",c)

def main():
    add()
    sub()
    if __name__==__main__:
        main()
# main()

##############

first.py ( Working with the created module )

from calc import *

#print("first says : ",__name__)

def one():
    add(10,12)
one()

################
