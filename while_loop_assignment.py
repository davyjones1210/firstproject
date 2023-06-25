#calculate sum of positive integers from the loop
#if user enters 0, exit from the loop

total=0
number = int(input("Enter a number (0 to quit): "))
while number !=0 :
    print(number)
    if number >0:
        total += number
    number = int(input("Enter a number (0 to quit): "))
else:
    print("In else block")
    print("Total is: ", total)
print("Out from loop")
# while count > 0:
#    print(count)
#    count -=1
#    if count == 3:
#        break
# else:
#    print("In else block")
# print("Out from loop")
