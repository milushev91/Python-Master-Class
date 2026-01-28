def fibonacci(n: int) -> any:
    """
    Generates a fibonacci sequence until last number > n, when value greater than 1 is given,
    returns n. Raises ValueError if negative value of n is recieved. 
    
    :param n (int): Represents the end point of the sequence with n exsclusive.
    :return (str): Fibonacci sequence represented as String or n as Integer.
    """

    if n < 0:
        raise ValueError("Negative number not allowed!")
    
    if 0 <= n <= 1:
        return n
    numbers = [0, 1]
    number = 0
    index = 1

    while True:
        number = numbers[index] + numbers[index - 1]
        if number > n:
            break
        numbers.append(number)
        index += 1
    
    return [str(num) for num in numbers]

print(fibonacci("str"))
