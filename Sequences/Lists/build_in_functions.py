even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# min function returns the smallest element in the list, if list is empty it raises a ValueError
# max function returns the largest element in the list, if list is empty it raises a ValueError
print(min(even)) # Outputs: 2
print(min(odd)) # Outputs: 1
print(max(even)) # Outputs: 8
print(max(odd)) # Outputs: 9

print()

#len function returns the number of elements in the list, if list is empty it returns 0
print(len(even)) # Outputs: 4
print(len(odd)) # Outputs: 5

print()

#count method returns the number of occurrences of a specified value in the list
#or 0 if the value is not found

print("mississippi".count("s")) # Outputs: 4
