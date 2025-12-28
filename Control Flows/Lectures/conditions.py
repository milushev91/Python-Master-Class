age = int(input("How old are you? "))

# and operator is true if both conditions are true
if age >= 16 and age <= 65:
    print("Have a nice day at work!")

print("-" * 80)

#simplified version using chained comparison
if 16 <= age <= 65:
    print("Have a nice day at work!")
else:
    print("Enjoy your free time!")

print("-" * 80)

# or operator is true if at least one condition is true
if age < 16 or age > 65:
    print("Enjoy your free time!")
else:
    print("Have a nice day at work!")

print("-" * 80)


