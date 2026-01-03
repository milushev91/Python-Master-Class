numbers = input("Please enter series of numbers with any separators you like: ")

separators = ""

for char in numbers:
    if not char.isnumeric():
        separators += char

print(separators)

values = [int(char) for char in numbers if char.isnumeric()]

#sum function adds all the items in an iterable and returns the total
print(sum(values))
