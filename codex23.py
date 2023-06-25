#WAP that will convert given marks in into grades
#students and marks given, grade scale given - convert marks to grades
student_marks = {
    "Jenny":92,
    "Harry":78,
    "Dimpy":56,
    "Rahul":41,
    "Aniket": 99,
    "Prem":34
}

grade=''
student_grades = {}
#print(student_marks)
#print(type(student_grades))
def calc_grades(marks):
    #for value in student_marks.values():
     if marks < 40:
         grade = "F"
         return grade
     elif 40 <= marks <= 50:
         grade = "D"
         return grade
     elif 51 <= marks <= 60:
         grade = "C"
         return grade
     elif 61 <= marks <= 70:
         grade = "B"
         return grade
     elif 71 <= marks <= 80:
         grade = "B+"
         return grade
     elif 81 <= marks <= 90:
         grade = "A"
         return grade
     elif 91 <= marks <= 100:
         grade = "A+"
         return grade

student_grades = student_marks.copy()

for k,v in student_marks.items():
    grade = calc_grades(v)
    student_grades[k]=grade
print(student_marks)
print(student_grades)





