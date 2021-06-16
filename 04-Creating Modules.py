# Module ( By Creating modules we can create our own muliple functions, class ,objects which can be used further if needed)

#wroking area 

from Calc import * #( * importing all) # import Calc or from Calc import add 

a = 9
b = 7

c = sub(a,b)

print(c)

# Calc.py (our created module)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b
