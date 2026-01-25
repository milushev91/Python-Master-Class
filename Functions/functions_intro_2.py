#function declarations can include or not include parameters.
#paramets are variables that act as placeholders for the values 
# that you pass to a function when you call it.
# this allows you to pass different values to the same function,
# making the function more flexible and reusable.
def multiply(x, y):
    result = x * y
    return result

#when parameters are used in a function definition,
# you must provide corresponding arguments when calling the function.
# these arguments are the actual values that get passed to the function.
# if not enough arguments are provided, or if too many are given,
# Python will raise a TypeError.
answer = multiply(10.5, 4)
print(answer)  # This will output: 42.0

forty_two = multiply(6, 7)
print("The answer is:", forty_two) # This will output: The answer is: 42

#function calls are also type of expression that can be used anywhere expressions are allowed.
#in the example below, we use the multiply function inside a for loop
for val in range(1, 5):
    two_times = multiply(2, val)
    print("2 times", val, "is", two_times)
