marks = int(input("Enter marks : "))

grade = ""

if marks >= 90:
    grade = "A"
elif 89 >= marks >= 80:
    grade = "B"
elif 79 >= marks >= 70:
    grade = "C"
elif 69 >= marks >= 60:
    grade = "D"
elif 59 >= marks >= 50:
    grade = "E"
else:
    grade = "F"

print("Your grade is :", grade)

# Enter marks : 95
# Your grade is : A