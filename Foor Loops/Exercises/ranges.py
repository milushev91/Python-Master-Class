#range object can be used in for loops to generate a sequence of numbers
# The range() function can take one, two, or three arguments:
# range(stop) - generates numbers from 0 to stop-1
# range(start, stop) - generates numbers from start to stop-1
# range(start, stop, step) - generates numbers from start to stop-1, incrementing by step
# using a negative step will generate numbers in descending order
# normally i isn't appropriate variable name, but it is a convention for loop counters
# if nested loops we can use j, k, etc.
for i in range(1, 21):
    print(i)
