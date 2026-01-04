import random

#we can use functions inside random module using dot notation
#dot notation tells Python that it can find randint function
#inside the random module
#randint function returns random number in range including end point

LOWEST = 1
HIGHEST = 10

#generate random number
answer = random.randint(1, 10) 
print(answer) #TODO:Remove after testing!

user_guess = None

#repeat until user guess is correct
while user_guess != answer:
    user_guess = int(input("Please guess a number between {} and {} or 0 to quit: ".format(LOWEST, HIGHEST)))

    #exit if 0 is typed
    if user_guess == 0:
        print("You exited the game!")
        break
    
    #display win message if user guess is correct
    if user_guess == answer:
        print("Congratulations. You got it right!")
        break

    if user_guess > answer:
        print("Please guess lower!")
    else:
        print("Please guess higher!")


