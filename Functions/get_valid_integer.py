def get_integer(prompt):
    while not prompt.isnumeric():
        prompt = input("Please enter an integer: ")
    return int(prompt)


integer = get_integer(input("Please enter an integer: "))
print(integer)
