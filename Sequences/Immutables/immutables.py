result = True
another_result = result
# id function returns the identity of an object
# which is unique and constant for this object during its lifetime.
# identity refers to the memory address where the object is stored.
print(id(result))
print(id(another_result))

result = False
print(id(result)) # New memory address since the value has changed

result2 = "Correct"
another_result2 = result2
print(id(result2)) # Memory address of "Correct"
print(id(another_result2)) # Same memory address as result2

result2 += "ish"
# The += operator creates a new string object since strings are immutable
# and assigns it to result2
print(id(result2)) # New memory address since the value has changed
print(id(another_result2)) # Same memory address as before
