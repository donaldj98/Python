# Without Function
a = 0
b = 1
x=int(input("Enter the number"))
print(a)
print(b)
for i in range(2,x):
    c=a+b
    print(c)
    a=b
    b=c
    print(c)
    
# With Function

def fib(n):

    a = 0
    b = 1

    if n == 1:
        print(a)

    else:
        print(a)
        print(b)

    for i in range(2,n):
        c = a + b
        a = b
        b = c
        print(a+b)

fib(100)
