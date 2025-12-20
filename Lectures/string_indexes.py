#Strings are sequence of characters used to store and
# represent text-based data.
#In Python, strings are indexed, meaning each character 
# in a string has a unique position or
# index that can be used to access or manipulate it.
#String indexing starts at 0 for the first character,
# 1 for the second character, and so on.

         #012345678910111213
parrot = "Norwegian Blue"

print(parrot)          # Output: Norwegian Blue
#Accessing character on fourth position using bracket notation
#and index 3
print(parrot[3])       # Output: w

#print(parrot[16])      # This will raise an IndexError:
#string index out of range
#because the index 16 is out of range for the string "Norwegian Blue"

#Challenge: print we win, each character on a new line
print(parrot[4])   # Output: e
print(parrot[9])   # Output:
print(parrot[3])   # Output: w
print(parrot[6])  # Output: i
print(parrot[8])  # Output: n
