numbers = [1, 45, 31, 12, 60]

for number in numbers:
    if number % 8 == 0:
        #reject the list
        print("The number is unacceptable!")
        break
#else clause runs if the loop completes normally
else:
    print("All numbers are acceptable!")
