print("\t \t \t Multiplication Table", end = "   ")

print(" ")
print(" ")

multiple = 1

for counter in range(1, 10):

    print(f"    {counter}", end= "\t")

print("")
print(" _"* 38)
print(" ")

#for index in range (1, 10):
#
#    print(f"{index}", end=" |\n")
#
#print(" ")

   

    

for count in range(1, 10):

    print(f"{count}", end="|\t")

    for number in range(1, 10):

        multiple = count * number

        print(f"{multiple}", end="\t")
                      
    print("")

