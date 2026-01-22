numbers = input("Please enter three numbers, separated by commas: ").split(",")

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

a, b, c = numbers

print(a + b - c)
