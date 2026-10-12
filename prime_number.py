#PSUEDO CODE

#Prime numbers are numbers that are divisible by one and itself


#1. Collect number from the user
#2. Store the value collected in a container named number 
#3. set a range to compare the number with other numbers below the number inputed which is 2 till number 
#4. now compare the number one by one with the number inputed and see if it is divisible 
#5. Now output if the number is prime and if it is print true




number = int(input("Enter a prime number: "))

for index in range(2, number):

    if number % index != 0:

        print("True")
    

