sentence = input("Enter a sentence: ").lower()

count = 0

for letter in sentence:

    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":

        count += 1

print(count)
