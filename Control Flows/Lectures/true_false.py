day = "Monday"
temperature = 30
raining = True 

#Example of complex boolean expression
#When writing complex boolean expressions, 
#use parentheses to make your code more readable
#even when not strictly necessary
#in the example bellow and has higher precedence than or
#but using parentheses makes it clear what the intention is
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")

#Python False values: None, False, 0, "", [], (), {}
#Everything else is True

#Example 

name = input("Enter your name: ")

if name:
    print("Hello {}".format(name))
else:
    print("Are you the man with no name?")
