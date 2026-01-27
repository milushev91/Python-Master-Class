def get_integer(prompt):
    """
    Get integer from Standard Input(stdin).

    The function will continue looping, and prompting the user,
    until valid `int` is entered.
    
    :param prompt: The String that the user will see, when they are prompted
        to enter a value.
    :return: The integer that the user enters
    """
    while not prompt.isnumeric():
        prompt = input("Please enter an integer: ")
    return int(prompt)

integer = get_integer(input("Please enter an integer: "))
print(integer)
