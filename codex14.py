#Program to calculate average height
# from list of heights and take input from user
#output should be rounded to nearest whole number
#list = [151,153,140,160,167]
heights=input("Enter all heights seaparted by space: ")
height_list = heights.split(',')
print(height_list)
count=0
for height in height_list:  #for loop to calculate length of list
    count += 1
print(count)
for i in range(0, count):
    height_list[i]=int(height_list[i])

print(height_list)
total = 0
for person in height_list:
    total += person

avg= total/count
print(round(avg))