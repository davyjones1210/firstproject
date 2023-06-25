# list1=["Hi", "hello", "welcome"]
# names=["Krishna", "Ram", "Madhav"]
# for item in list1:
#     for name in names:
#         print(item,name)
#         if item =="hello" and name=="Ram":
#             break
#     print("Out from inner loop")
# print("Out from outer loop")



count=1
while count <=10:
    print(count)
    count +=1
    if count == 7:
       pass
       #continue
    print("Hi")
else:
  print("In else block")
print("Out from loop")


# for i in range(1,11):
#     if i==7:
#         #continue
#         pass
#     else:
#         print(i)