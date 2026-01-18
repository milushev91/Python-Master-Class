computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

#replacing an item in the list by index
computer_parts[3] = "trackball"
print(computer_parts)  # ['computer', 'monitor', 'keyboard', 'trackball', 'mouse mat']

#replacing a slice of the list with iterable
computer_parts[3:] = ["trackball", "power supply"]
print(computer_parts)  # ['computer', 'monitor', 'keyboard', 'trackball', 'power supply']

data = [4, 5, 104, 105, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

# del data[0:2]  # deleting first two items
# print(data)  # [104, 105, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]4

# del data[14:]  # deleting items from index 14 to end
# print(data)  # [104, 105, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]

#automated removal of items based on condition

min_value = 100
max_value = 200

# This approach can lead to skipping elements due to index shifting after deletion
# so for example when we remove 4 at index 0, 5 moves to index 0, but the loop moves to index 1 next,
# thus skipping the new item at index 0.
# for index, value in enumerate(data):
#     if value < min_value or value > max_value:
#         del data[index]

# print(data) # [5, 104, 105, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 360]

#safely removing items. Applicable with sorted lists

stop = 0

for index, value in enumerate(data):
    if value >= min_value:
        stop = index
        break

del data[:stop]
print(data)  # [104, 105, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191, 350, 360]

start = len(data)
for index in range(len(data)-1, -1, -1):
    if data[index] <= max_value:
        start = index + 1
        break

del data[start:]
print(data)  # [104, 105, 120, 130, 130, 150, 160, 170, 183, 185, 187, 188, 191]

