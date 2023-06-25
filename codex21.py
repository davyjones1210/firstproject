import math
def paint_calculation(h,w,c):
    area = h*w
    no_of_cans = area/c
    print(no_of_cans)
    print(f"You need to buy {math.ceil(no_of_cans)} cans")





h=4 #int(input...
w=20 #int(input...

coverage = 7

paint_calculation(h,w,coverage)
