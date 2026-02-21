filename = "./Jabberwocky.txt"

with open(filename) as poem:
    # Read the first line and strip the newline character
    # rstrip() removes any trailing whitespace characters, 
    # such as spaces and newlines, from the end of the string
    # including the newline character
    first = poem.readline().rstrip()
print(first)

chars = "'"
no_appostrophe = first.strip(chars)
print(no_appostrophe)

chars1 = "'Twasebv"
# strip() removes any leading and trailing characters 
# specified in the argument from the string.
# it removes all occurrences of the specified characters
#  from the beginning and end of the string until it
#  encounters a character that is not in the specified set.
no_twasebv = first.strip(chars1)
print(no_twasebv)
