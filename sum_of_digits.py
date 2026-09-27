number = int(input("Enter a number: "))

count = 0

while number > 0:
    
    last_number = number % 10

    count += last_number

    number = number // 10

print(count)
