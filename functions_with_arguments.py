# def greet(name,subject, dept="CS"):
#     print("Hi ", name)
#     print(f"You are from {dept} dept")
#     print(f"Do you teach {subject}? ")
#
# greet("Jenny","Python", "ME")

#Addition with functions - sum of 2 numbers

total = 0
def addition(*numbers):
    c=0
    for i in numbers:
        c += i
    print("Total is: ", c)


    #total = num1 + num2


    #print("The sum of two numbers is: ", total)
    #return total
#final_total = addition(4,5)
#print("The sum of two numbers is: ", final_total)
addition(4,5,6)
addition(5,7)
