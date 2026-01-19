empty_list = []
even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)  # Output: [[2, 4, 6, 8, 10], [1, 3, 5, 7, 9]]

for sublist in numbers:
    for number in sublist:
        print(number)
