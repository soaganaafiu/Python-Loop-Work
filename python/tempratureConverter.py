temperature_in_celsius = float(input("Enter the temprature in celsius: "))

if temperature_in_celsius <= -273:
    print("Impossible")

else:

    temperature_in_fahrenheit = temperature_in_celsius * (9 / 5) + 32

    for counter in range(int(temperature_in_fahrenheit) + 1, int(temperature_in_fahrenheit) + 6):
        print(counter)
