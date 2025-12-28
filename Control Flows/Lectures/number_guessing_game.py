answer = 5 

user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess == answer:
    print("Congratulations. You got it right!")
else:

    if user_guess > answer:
        print("Too High!")
    else:
        print("Too Low!")

    guess = int(input())

    if guess == answer:
        print("Congratulations. You got it right!")
    else:
        print("Sorry, you have not guessed correctly.")

# if user_guess != answer:

#     if user_guess > answer:
#         print("Too High!")
#     else:
#         print("Too Low!")

#     user_guess = int(input("Guess again: "))

#     if user_guess != answer:
#         print("Sorry, you have not guessed correctly.")
#     else:
#         print("Congratulations. You got it right!")
# else:
#     print("Congratulations. You got it right!")

# if user_guess > answer:
#     print("Too High!")

#     user_guess = int(input("Guess again: "))

#     if user_guess == answer:
#         print("Congratulations. You got it right!")
#     else:
#         print("Sorry, you have not guessed correctly.")

# elif user_guess < answer:
#     print("Too Low!")

#     user_guess = int(input("Guess again: "))
    
#     if user_guess == answer:
#         print("Congratulations. You got it right!")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("Congratulations. You got it right!")
