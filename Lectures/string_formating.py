for i in range(1, 13):
    #To set the field width use a number after the colon
    #By default the text is right aligned
    #To right align the text use the > character
    print("No. {0:2} squared is {1:3} and cubed is {2:4}"
          .format(i, i**2, i**3))

print()

for i in range(1, 13):
    #To left align the text use the < character
    #To center align the text use the ^ character
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}"
          .format(i, i**2, i**3))

print()

print("Pi is approximately {0:12}".format(22/7))
#To specify the number of digits after 
# the decimal point use . followed by the number of digits
#f is used to format a number as a fixed point number
#Maximum precision for a float is 50 digits
print("Pi is approximately {0:12f}".format(22/7))
print("Pi is approximately {0:12.50f}".format(22/7))
print("Pi is approximately {0:52.50f}".format(22/7))
print("Pi is approximately {0:62.50f}".format(22/7))
print("Pi is approximately {0:72.50f}".format(22/7))
print("Pi is approximately {0:<72.54f}".format(22/7))

print()

for i in range(1, 13):
    #You can also omit the positional arguments
    #In this case the arguments are used in the order they are passed to format()
    #You can still use the field width specifiers
    print("No. {} squared is {} and cubed is {:<4}"
          .format(i, i**2, i**3))
