weight = float(input("Enter weight : "))
height = float(input("Enter height : "))

bmi = (weight)/(height**2)

if bmi < 19:
    print("Underweight")
elif bmi >= 19 and bmi <= 25:
    print("Healthy")
else:
    print("Overweight")
