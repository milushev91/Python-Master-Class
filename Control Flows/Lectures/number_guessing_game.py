answer = 5 

user_guess = int(input("Guess a number between 1 and 10: "))

if user_guess > answer:
    print("Too High!")
elif user_guess < answer:
    print("Too Low!")
else:
    print("Congratulations. You got it right!")
