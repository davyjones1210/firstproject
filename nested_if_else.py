height = int(input("Enter height in feet: "))

if(height >= 3):
    print("You can ride")
    age = int(input("Enter age in yrs: "))
    if (age < 12):
        print("Pay $150")
    elif (18 > age > 12):
        print("Pay $250")
    elif (18 <= age):
        print("Pay $500")
else:
   print("Cannot ride")
print("Bye")