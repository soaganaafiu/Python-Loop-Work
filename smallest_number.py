number = int(input("Enter Number "))

smallest = 9

while number > 0:

    last_digit = number % 10

    if last_digit < smallest:
        
        smallest = last_digit

    number = number // 10

print(smallest)
