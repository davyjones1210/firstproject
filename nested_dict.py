# student_data = {
#     "Ram":{"roll_no":10,"age":20,"course":"Python"},
#     "Mohan":{"roll_no":20,"age":22,"course":"Java"},
# }

# # print(student_data["Mohan"])
# # print(student_data["Mohan"]["roll_no"])
# student_data["Mohan"]["phone_no"] = 987654
# print(student_data["Mohan"])
# #del student_data["Mohan"]["phone_no"]
# print(student_data["Mohan"].pop("phone_no"))
# print(student_data["Mohan"])


# travel_data = {
#     "Gujarat":["Dwarka","Somnath","Statue of unity"],
#     "Rajasthan":["Jaipur","Udaipur"]
# }
#
# #print(travel_data)
# print(travel_data["Rajasthan"])

student_data = [
    {
        "Name":"Ram",
        "roll_no":10,
        "age":20,
        "course":"Python"
     },
    {
        "Name":"Mohan",
        "roll_no":20,
        "age":22,
        "course":"Java",
        "Phone_no":[1234567,998766]
     }
]
#print(student_data)
print(student_data[1]["Phone_no"])

def add_new_student(name,roll_no,age,course_opted):
    new_student={}
    new_student["Name"] = name
    new_student["roll_no"] = roll_no
    new_student["age"] = age
    new_student["course"] = course_opted
    student_data.append(new_student)
    print(student_data)



add_new_student("Shyam",22,18,"C++")