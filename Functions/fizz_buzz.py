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

input("Play Fizz Buzz.   Press ENTER to start ")
print()

next_number = 0 

while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("You go: ")
    if correct_answer != player_answer:
        print("You lose. The correct answer is {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}.".format(next_number))
