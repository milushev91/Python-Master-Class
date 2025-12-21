age = 24 
#Every data type can be converted to string using str() function
print("My age is " + str(age) + " years") # Output: My age is 24 years
#But if we use a lot of variables then it becomes hard to read
#Instead we can use .format() function
#{} is used as a placeholder
#Number inside {} represents the index of the value passed in .format()
#The values inside .format() will be placed in the respective placeholders

print("My age is {0} years".format(age)) # Output: My age is 24 years
#Multiple placeholders can be used
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}."
      .format(31, "January", "March", "May", "July", "August", "October", "December"))
# Output: There are 31 days in January, March, May, July, August, October and December.

#The order of indexes inside placeholders can be changed
print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}"
    .format(28, 30, 31))
# Output: Jan: 31, Feb: 28, Mar: 31, Apr: 30, May: 31, Jun: 30, Jul: 31, Aug: 31, Sep: 30, Oct: 31, Nov: 30, Dec: 31

#.format() can be used with triple quotes as well
print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1}
Jul: {2}
Aug: {2}
Sep: {1}
Oct: {2}
Nov: {1}
Dec: {2}"""
    .format(28, 30, 31))
#Output:
#Jan: 31
#Feb: 28
#...
