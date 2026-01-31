def factorial(num: int) -> int:
    """
    Finds number factorial.
    
    :param num: integer number.
    :return: factorial of the number as integer.
    """

    if num == 0:
        return 1
    result = 1
    for i in range(2, num + 1):
        result *= i 
    
    return result

for i in range(36):
    print("{} {}".format(i, factorial(i)))
