def fizz_buzz(number: int) -> str:
    """
    Checks number whether it is divisible by 3 and returns 'fizz', by 5 - 'buzz' or
    both - 'fizzbuzz'. In any other case it returns the number as string
    
    :param number: Integer number
    :type number: int
    :return: 'fizz', 'buzz' or str(number)
    :rtype: str
    """
    if number % 5 == 0 and number % 3 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

for num in range(1, 101):
    print(fizz_buzz(num))
