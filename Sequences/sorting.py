#pangram is a sentence that contains every letter of the alphabet at least once
pangram = "The quick brown fox jumps over the lazy dog"

# sorted function sorts the characters of the string in ascending order
# it can recieve any iterable and returns a list of sorted elements
# it does not modify the original string, as strings are immutable in Python
letters = sorted(pangram)
print(letters)
#spaces come first in ASCII order, followed by uppercase letters, then lowercase letters
#so the output will have all spaces first, then 'T', then all other letters in order
#if other characters were present, they would be sorted according to their ASCII values as well
print(''.join(letters)) #Output: '        Tabcdeeefghhijklmnoooopqrrsttuuvwxyz'

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
#you can sort numbers as well
#sorted returns a list of numbers in ascending order
sorted_numbers = sorted(numbers)
print(sorted_numbers) #Output: [1.6, 2.3, 3.1, 4.5, 8.7, 9.2]
print(numbers) #Original list remains unchanged: [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]

#the sort method sorts the list in place and modifies the original list
#it returns None
#so you should not assign its result to a variable
numbers.sort()

print(numbers) #Output: [1.6, 2.3, 3.1, 4.5, 8.7, 9.2]



