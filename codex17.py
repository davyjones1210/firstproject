#WAP that will print number from 1 to n (100)
#numbers that are divisible by 3, print fizz
#numbers divisible by 5, print buzz
#numbers both divisible by 3 AND 5, print fizz buzz

for i in range(1,101):
    if ((i % 3 == 0) and (i % 5 == 0)):
        print("fizz buzz")
    elif i%3==0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")

    else:
        print(i)

