first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))


largest = first_number

if largest < second_number:
    largest = second_number

if largest < third_number:
    largest = third_number

print(largest)
