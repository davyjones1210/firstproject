# def add(*numbers, name):
#     c=0
#     print(name)
#     for i in numbers:
#         c +=i
#     print(f"The sum is: {c}")
#
# add(1,2, name = "Jenny")
# add(6,5,6)
# add(1,2,3,4,56,8)

#Now passing info of a person

def info_person(*args,**kwargs):
    for key,value in kwargs.items():
        print(key,value)
        print(args)

info_person(1,2, name="Ram", age=30, dept="CS")
info_person(1,2,3,name="Shyam", dept="CS")
