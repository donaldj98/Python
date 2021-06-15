# Lambda function ( anonymous function)

# def square(a):
#     return a * a
#
# result = square(5)
#
# print(result)

e = lambda a: a*a
f = lambda a,b : a+b

square = E(5)
result = f(5,6)

print(square)
print(result)

# Using Filter, Map and Reduce (used in Google maps for filtering, modifing and reducing)

nums = [3,2,6,8,4,6,2,9]

evens = list(filter(lambda n : n%2==0,nums))

doubles = list(map(lambda n : n*2,evens))
print(doubles)


from functools import reduce # reduce is not a inbuit function so its imported
sum = reduce(lambda a,b : a+b,doubles)

print(sum)
