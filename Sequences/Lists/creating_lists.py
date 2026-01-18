#creating lists in Python with different methods
#create empty list with literals
empty_list = []
#create list with values using literals
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

#create list by concatenation of two lists or more using +
#order matters in concatenation first list items will appear first then second list items and etc.
numbers = even + odd
print("Concatenated List:", numbers) #Output: Concatenated List: [2, 4, 6, 8, 1, 3, 5, 7, 9]

sorted_numbers = sorted(numbers)
print(sorted_numbers) #Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

digits = sorted("432985617")
#when you create a list from certain type then all items in the list will be of that type
print(digits) #Output: ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#create list using list() constructor
more_numbers = list(numbers)
print(more_numbers) #Output: [2, 4, 6, 8, 1, 3, 5, 7, 9]

#when creating a list using list() constructor a new list object is created in memory
#even though the contents are the same as the original list
print(more_numbers == numbers) #Output: True
#is operator checks if both variables point to the same object in memory
print(more_numbers is numbers) #Output: False

#create a copy of a list using copy() method
another_numbers = numbers.copy()
print(another_numbers == numbers) #Output: True
print(another_numbers is numbers) #Output: False

#create a copy of a list using slicing
yet_another_numbers = numbers[:]
print(yet_another_numbers == numbers) #Output: True
print(yet_another_numbers is numbers) #Output: False
