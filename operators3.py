#a,b = 5,6
a = 5
#print(a is b)
print(id(a))
a = 8
print(id(a))
print(a is a)