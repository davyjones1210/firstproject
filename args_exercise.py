def multiply(*args):
    total=1
    for i in args:
        total = total*i
    print("The total is: ", total)


multiply(2,3,-6,8)
multiply(2,5,8,9,1,6)