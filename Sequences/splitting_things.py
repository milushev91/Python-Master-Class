panagram = "The quick brown fox jumps over the lazy dog"
# split is str method that splits a string into a list where each word is a list item
# It takes one optional argument, separator (sep) which specifies 
# the character to use for splitting the string
# By default, split() splits the string at each space this includes spaces, tabs, and newlines
# list items in the created list are of type str
words = panagram.split()
print(words) #['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

numbers = "1,2,3,4,5,6,7,8,9,10"
# Here we are specifying ',' as the separator
num_list = numbers.split(',')
print(num_list) #['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

generated_list = " ".join(num_list).split()
print(generated_list) #['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

generated_list_length = len(generated_list)

# for i in range(generated_list_length):
#     generated_list[i] = int(generated_list[i])
# print(generated_list) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = []

for item in generated_list:
    new_list.append(int(item))
