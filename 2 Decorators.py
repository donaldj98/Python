# Decorators (without modifing the real function we can change the exsiting function using decorators)

# def div(a,b):
#     print(a/b)
#
# div(2,4)


# def div(a,b):
#     if a<b:
#         a,b = b,a
#     print(a/b)
#
# div(2,4)

def div(a,b):
    print(a/b)

def smart_div(func): # only in python - function inside a function because everything in python is object

    def inner(a,b):

        if a<b:
            a,b = b,a
        return func(a,b)

    return inner

div = smart_div(div)

div(2,4)
