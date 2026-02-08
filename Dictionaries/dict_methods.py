d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

#.fromkeys() is dict class method that creates a new dictionary
#  with keys from an iterable and values set to a specified value (default is None).
new_dict = dict.fromkeys(pantry_items, 0)
print(new_dict) # Output: {'chicken': 0, 'spam': 0, 'egg': 0, 'bread': 0, 'lemon': 0}

#.keys() is a dictionary method that returns a view object containing the keys of the dictionary.
# The view object is dynamic and reflects changes to the dictionary.
# When printed, it displays the keys in a list-like format.
d_keys = d.keys()
print(d_keys) # Output: dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# you can iterate over the keys of the dictionary using a for loop
# some programmers prefer to use .keys() method to make it explicit
#  that they are iterating over the keys of the dictionary, while others may choose to iterate directly over the dictionary itself, which also yields the keys by default.
for key in d.keys():
    print(key) # Output: 0 1 2 3 4 5 6 7 8 9 (each on a new line)   

d2 = {
    7: "lucky seven",
    10: "ten",
    3: "this a new three"
}

#.update() is a dictionary method that updates the dictionary with key-value
#  pairs from another dictionary or an iterable of key-value pairs.
# If a key already exists in the dictionary, its value will be updated with 
# the new value from the provided dictionary.
# Insertion order is preserved in Python 3.7 and later versions, meaning 
# that the order of key-value pairs in the updated dictionary 
# will reflect the order in which they were added.
#updating dictionary d with key-value pairs from dictionary d2
d.update(d2)
print(d) # Output: {0: 'zero', 1: 'one', 2: 'two', 3: 'this a new three', 4: 'four', 5: 'five', 6: 'six', 7: 'lucky seven', 8: 'eight', 9: 'nine', 10: 'ten'}

# you can also use .update() to add key-value pairs from an iterable 
# of key-value pairs, such as a list of tuples or the result of the enumerate() function.
d.update(enumerate(pantry_items))

for key, value in d.items():
    print(f"{key}: {value}") # Output: 0: zero
                             #         1: one   

# returns a view object containing the values of the dictionary. 
# The view object is dynamic and reflects changes to the dictionary. 
# When printed, it displays the values in a list-like format.
d_values = d.values()
print(d_values) # Output: dict_values(['zero', 'one', 'two', 'this a new three', 'four', 'five', 'six', 'lucky seven', 'eight', 'nine', 'ten', 'chicken', 'spam', 'egg', 'bread', 'lemon'])
