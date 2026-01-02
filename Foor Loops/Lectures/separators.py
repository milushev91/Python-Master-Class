numbers = "9,223;372:036 854,775;807"
separators = ""

for char in numbers:
    #isnumeric() method returns True if the string is a number
    if not char.isnumeric():
        separators += char

print(separators)
