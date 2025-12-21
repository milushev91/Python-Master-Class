#Code Blocks

#Create a code block with for loop
#: marks the beginning of the block
#after which all lines indented by the same number
#of spaces are part of the block
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}"
    .format(i, i**2, i**3))
#To remove indentation, use backwards tab
#To indent, use tab or 4 spaces
print("*" * 80) #Output: a line of 80 asterisks
