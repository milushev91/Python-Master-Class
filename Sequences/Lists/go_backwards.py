data = [101, 104, 4, 105, 185, 120, 130, 150, 160, 170, 183, 187, 188, 191, 350, 360]

min_value = 100
max_value = 200 

# Safely removing items by iterating backwards
# for index in range(len(data)-1, -1, -1):
#     if data[index] < min_value or data[index] > max_value:
#         del data[index]

# Alternative method using reversed and enumerate
# its slightly less efficient due to the overhead of enumerate and reversed
# but often more readable
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_value or value > max_value:
        del data[top_index - index]
print(data)  # Output the modified list
# Output: [101, 104, 105, 185, 120, 130, 150, 160, 170, 183, 187, 188, 191]
