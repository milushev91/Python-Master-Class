def sum_numbers(*args: float) -> float:
    """
    Finds the sum of serie of numbers.
    
    :param args: Serie of numbers.
    :type args: float.
    :return: The sum of the serie of numbers.
    :rtype: float.
    """
    sum_nums = 0
    for num in args:
        sum_nums += num
    return sum_nums
