

day_of_the_week = int(input("Enter the day of the week: "))

number = day_of_the_week % 7

if number == 1:
    print("Monday")
elif number == 2:
    print("Tuesday")
elif  number == 3:
    print("Wednesday")
elif  number == 4:
    print("Thursday")
elif  number == 5:
    print("Friday")
elif  number == 6:
    print("Saturdday")
else:
    print("Sunday")

