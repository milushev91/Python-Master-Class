#String negative indexes
# In Python, strings can also be indexed using negative numbers.
# Negative indexing allows you to access characters from the end of the string,
# where -1 refers to the last character, -2 to the second last, and so on.

parrot = "Norwegian Blue"

print(parrot[-1])   # Output: e
print()
#Challenge: print we win, each character on a new line using negative indexes

print(parrot[-11])  # Output: w 
print(parrot[-10])  # Output: e
print(parrot[-5])   # Output: 
print(parrot[-11])  # Output: w 
print(parrot[-8])   # Output: i
print(parrot[-6])   # Output: n

#Negative index can be uptained by subtracting the 
# length of the string from the positive index.
print()
print(parrot[3 - 14])       # Output: w
print(parrot[4 - 14])   # Output: e
print(parrot[9 - 14])   # Output:
print(parrot[3 - 14])   # Output: w
print(parrot[6 - 14])  # Output: i
print(parrot[8 - 14])  # Output: n
