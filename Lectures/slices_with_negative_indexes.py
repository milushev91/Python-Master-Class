         #012345678911234
parrot = "Norwegian Blue"

# Python slicing reminder:
# sequence[start : stop : step]
#
# Default step is +1 (left → right):
# - start index must be LEFT of stop index
# - otherwise, slice is empty
#   e.g. text[-4:12]  -> works
#        text[-4:2]   -> empty
#
# Reverse slicing:
# - use a negative step (-1)
# - start index must be RIGHT of stop index
#   e.g. text[-4:2:-1] -> works
#
# Negative indexes are resolved first,
# then slicing direction rules are applied.

print(parrot[-4:2]) # Output: 
print(parrot[-4:2:-1]) # Output: B naigew

print(parrot[-4: -2]) # Output: Bl
print(parrot[-4: 12]) # Output: Bl

#Challenges
print(parrot[:6]) # Output: Norweg
print(parrot[-14:-8]) # Output: Norweg

print(parrot[3:5])    # Output: we
print(parrot[-11: -9])    # Output: we
print(parrot[0:9])    # Output: Norwegian
print(parrot[-14:-5])    # Output: Norwegian
print(parrot[10:]) #  Output: Blue
print(parrot[-4:]) #  Output: Blue
print(parrot[6:])  # Output: ian Blue
print(parrot[-8:])  # Output: ian Blue
