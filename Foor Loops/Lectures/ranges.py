#range object can be used in for loops to generate a sequence of numbers
# The range() function can take one, two, or three arguments:
# range(stop) - generates numbers from 0 to stop-1
# range(start, stop) - generates numbers from start to stop-1
# range(start, stop, step) - generates numbers from start to stop-1, incrementing by step
# if we want to use step their must start and stop values
# step can be positive or negative
# using a negative step will generate numbers in descending order
# normally i isn't appropriate variable name, but it is a convention for loop counters
# if nested loops we can use j, k, etc.
for i in range(1, 21):
    print(i)

for i in range(0, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

#we can also use range to check whether a number is in a specific range
#it is not the most efficient way, but it works
#but it is more readable than using comparison operators

number = 5

if number in range(1, 11):
    print(f"{number} is in the range")
