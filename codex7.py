#BMI = weight/height^2
weight = 70 #int(input("Weight = "))
height = 1.85 #float(input("Height = "))
bmi = round(weight/(height**2))
if (bmi < 18.5):
    print(f"Your BMI is {bmi} and you are underweight")
elif (bmi < 25):
    print(f"Your BMI is {bmi} and you are normal weight")
#print(bmi)
#print(round(bmi))
