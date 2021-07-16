# To Notify the end user about the error they are going through
# Synatx errors cannot be handled it the programmers duty to handle it properly

# x = 10
try :
  if x==10:
    print("X is 10")
except:
  print("variable Not Declared")      # If the try block fails then the except block executes and prints what we gave in print statement
     Or 
except Exception as e :               # Will give the proper info 
  print(e)

  

# To handle more exceptions for every syntax
 
try :
  if x==10:
    print("X is 10")
  sample = open('sample.txt',"r")
    
except Exception as e :              
  print(e)
# In the above case there are two error but one will be exceuted and the second will be ignored so seprate block should be used 
try :
  if x==10:
    print("X is 10")
#   sample = open('sample.txt',"r")#
    
except Exception as e :              
  print(e)

try :
  sample = open('sample.txt',"r")
    
except Exception as e :              
  print(e)
  
  
# Another example

def division (x,y):
  try :
    div=x/y
  except Exception as e: 
    print(e)
  else:                       # If there is no error in the exception block then the else part will be exceuted 
    print(div)
a=int(input("enter a : "))
b=int(input("enter b : "))
division(a,b)
    
def division (x,y):
  while True :
    try :
      div=x/y
    except Exception as e: 
      print(e)
      y=int(input("Enter a non zero value : ")
    else:                       # If there is no error in the exception block then the else part will be exceuted 
      print(div)
      break
    finally:                        # It will be always exceuted at the end when everything done right
      print("Code Exceuted Successfully") # It also can be used to close the opened file 
       
a=int(input("enter a : "))
b=int(input("enter b : "))
division(a,b)
    
  
