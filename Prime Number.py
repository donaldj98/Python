def Prime(x):
    for i in range(2,x):
        if x%i==0:
            print('Not an Prime Number')
            break
    else:
        print("It's an Prime Number")
Prime(8)
