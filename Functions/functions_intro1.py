#declaration of a function that multiplies two numbers
def multiply():
    # multiplication of 10.4 and 5 and binding the result to a variable called result
    result = 10.4 * 5
    #return key word to return the result of the function in this case the multiplication result
    return result
#after function declaration we leave two blank lines for better readability
#this is PEP 8 style guide recommendation

#to call the function we use the function name followed by parentheses
#in this case we are also binding the returned value to a variable called answer
#when we call the function multiply it will execute the code inside the function
#after execution it will return the result which will be stored in the variable answer
#variables declared inside a function are local to that function
#this means they cannot be accessed outside the function
#this is known as variable scope or in this case local scope
answer = multiply()
print(answer)  # this will output: 52.0

