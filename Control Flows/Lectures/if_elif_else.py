#if Statements
min_age = 18
#input function gets user input in string format
name = input("Please enter your name: ")
#Convert string to integer using int() function
#If the input is not a valid integer, it raises a ValueError
age = int(input("How old are you, {0}? ".format(name)))
print(age)

#if statement to check condition
#the code block inside the if statement
#is executed only if the condition is True
if age >= min_age:
    print("You are old enough to vote!") #Output: You are old enough to vote!
#else block is executed if the condition inside if statement is False
#in any other case the code block inside else is not executed
else:
    print("Please come back in {0} years.".format(min_age - age))

print()

#New if else construction marks the beggining of new check which
#is independent of the previous one
if age < 18:
    print("Please come back in {0} years.".format(min_age - age))
#elif check is used to check multiple conditions
#elif condition is checked only if the previous
#if or elif conditions were False
#if the elif condition is True,
#the code block inside it is executed
#and the rest elif or else blocks are skipped
#multiple elif checks can be used
elif age == 900:
    print("Sorry Yoda you died in Return of the Jedi.")
else:
    print("You are old enough to vote!")
