weight = float(input("What is your weight: "))
height = float(input("How tall are you: "))


bmi = weight/(height * height)

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal")
elif bmi < 29.9:
    print("Overweight")
elif bmi >= 30:
    print("Obese")
