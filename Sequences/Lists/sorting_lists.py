even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

#extend method adds all elements of an iterable (like another list) to the end of the list
#modifies the original list and returns None
#other iterables could be tuples, sets, or strings
#dictionaries would add only the keys
even.extend(odd)
print(even) # Outputs: [2, 4, 6, 8, 1, 3, 5, 7, 9]

#sort method sorts the elements of the list in ascending order
#modifies the original list and returns None
even.sort() 
print(even) # Outputs: [1, 2, 3, 4, 5, 6, 7, 8, 9]

#another_even is pointing to the same place in memory as even
another_even = even

#sort method can also take a reverse parameter
#if reverse is set to True, the list is sorted in descending order
even.sort(reverse=True)
print(even) # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1]

#since another_even points to the same list as even, it also gets the same changes as even
print(another_even) # Outputs: [9, 8, 7, 6, 5, 4, 3, 2, 1]
