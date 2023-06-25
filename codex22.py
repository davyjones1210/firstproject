#Find if number is a prime number
def prime_checker(number):
    for i in range(2,number):
        #print(i)
        if number%i == 0:
            print(f"{number} is a composite number")
            print(f"It is divisible by {i}")
            break

    else:
        print(f"{number} is a prime number")



n = 81 #int(input...
prime_checker(n)