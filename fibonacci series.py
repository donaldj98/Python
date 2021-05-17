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
