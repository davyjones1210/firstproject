#Program to calculate average height, then max height
# from list of heights and take input from user
#output should be rounded to nearest whole number
#list = [151,153,180,160,167]
heights=input("Enter all heights seaparted by space: ")
height_list = heights.split(',')
print(height_list)
count=0
for height in height_list:  #for loop to calculate length of list
    count += 1
#print(count)
for i in range(0, count):
    height_list[i]=int(height_list[i])

print(height_list)
total = 0
for person in height_list:
    total += person

avg= total/count
#print(round(avg))
compare=0
maximum=0
for i in range(0, count):
    #if i == 0:
        #compare = height_list[0]
    for j in range(0, count):
        if height_list[j] > height_list[i]:
            maximum = height_list[j]
print(maximum)