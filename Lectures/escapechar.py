# \n is the escape character for a new line in Python strings.
split_string = "This string has been\n split on\n several lines."
print(split_string)
# This string has been
# split on
# several lines.

# \t is the escape character for a tab in Python strings.
tabbed_string = "1\t2\t3\t4\t5"
print(tabbed_string) # 1	2	3	4	5

# you can use \ to escape characters in strings like single 
# and double quotes.

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# The pet shop owner said "No, no, 'e's uh,...he's resting".
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# The pet shop owner said "No, no, 'e's uh,...he's resting".

# if you use triple quotes, you don't need to escape single
# or double quotes inside the string.
print("""The pet shop owner said "No, no, 'e's uh,...he's resting". """)
# The pet shop owner said "No, no, 'e's uh,...he's resting".

# Triple quotes can also be used to create multi-line strings
another_split_string = """This string has been
split over
several lines."""

print(another_split_string)
#This string has been
#split over
#several lines.

#you can also use / to escape new line characters in your triple
#quoted strings.
yet_another_split_string = """This string has been \
split over \
several lines."""
print(yet_another_split_string)
#This string has been split over several lines.

#Escape character for backslash

# To include a backslash in a string, you need to escape it 
# with another backslash.
print("C:\\Users\\Temp\\Documents") # C:\Users\Temp\Documents
# Alternatively, you can use raw strings by prefixing the string
# with 'r' to avoid escaping backslashes.
print(r"C:\Users\Temp\Documents") # C:\Users\Temp\Documents


