bill = 0
height = int(input("Enter height in feet: "))

if(height >= 3):
    print("You can ride")
    age = int(input("Enter age in yrs: "))
    if (age < 12):
        print("Pay $150")
        bill = 150
    elif (18 > age > 12):
        print("Pay $250")
        bill = 250
    elif (18 <= age):
        print("Pay $500")
        bill = 500
    want_photo = input("Do you want to take photo? (y/n): ")
    if (want_photo == 'y' or want_photo == 'Y'):
        print("$50 will be added to your bill")
        bill = bill + 50
        print(f"Your bill is ${bill}")
    else:
        print(f"Your bill is ${bill}")
else:
   print("Cannot ride")
print("Bye")