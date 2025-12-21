age = 24
name = "Alice"
age_in_words = "2 years"

# Using f-strings to embed expressions inside string literals
print(name + f" is {age} years old.")  # Output: Alice is 24 years old.
print(f"Pi is approximately {22 / 7:12.50f}.") 
# Output: Pi is approximately 3.142857142857142857142857142857142857142857142857142857142857.

pi = 22/7

print(f"Pi is approximately {pi:.50f}.")
# Output: Pi is approximately 3.14285714285714283596573873136383104324340820312500.
