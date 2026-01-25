def add(x):
    return x + 1

def add_item(x):
    x.append(6)
    return x 

# pass by value
number = 2
number2 = add(number)
print(number, number2) # 2 3

numbers = [1, 2, 3, 4, 5]

# pass by refference
new_numbers = add_item(numbers)

print(numbers, new_numbers) # [1, 2, 3, 4, 5, 6] [1, 2, 3, 4, 5, 6]

