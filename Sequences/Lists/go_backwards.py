data = [101, 104, 4, 105, 185, 120, 130, 150, 160, 170, 183, 187, 188, 191, 350, 360]

min_value = 100
max_value = 200 

# Safely removing items by iterating backwards
for index in range(len(data)-1, -1, -1):
    if data[index] < min_value or data[index] > max_value:
        del data[index]
