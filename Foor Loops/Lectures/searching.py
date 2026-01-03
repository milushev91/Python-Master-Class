shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spams"
# None is used to represent 'no value' or 'not found'
# It is a special value in Python that means "nothing"
found_at = None
#len function gives the length of a sequence like a list
shopping_list_length = len(shopping_list)

# Loop through the list by index
# it is combined with range function since the loop will start at 0
# and go up to (but not including) the length of the list
for i in range(shopping_list_length):
    if shopping_list[i] == item_to_find:
        found_at = i
        # Exit the loop once the item is found
        # So we don't waste time continuing the
        # loop after we've found the item
        # it helps with efficiency
        break   

# In Python, the is operator is used to check object identity, not value equality.

# What that means

# is checks whether two variables refer to the exact same object in memory.

# It does not compare the contents or values of the objects.

# Syntax
# a is b

# Example
# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]

# print(x is y)  # True  → same object
# print(x is z)  # False → different objects, same values

# is vs ==
# Operator	Purpose
# is	Checks identity (same object in memory)
# ==	Checks equality (same value/content)
# print(x == z)  # True (values are equal)
# print(x is z)  # False (different objects)

# Common and correct use cases

# ✅ Checking against None

# if value is None:
#     print("No value provided")


# ✅ Singleton objects (True, False, None)

# a = None
# b = None
# print(a is b)  # True
# if found_at is not None:

if found_at:
    print(f"{item_to_find} is at index {found_at}")
else:
    print(f"{item_to_find} is not found!")

