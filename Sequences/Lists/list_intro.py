# creating a list of computer parts through direct assignment
computer_parts = ["computer", "monitor", "keyboard", "mouse", "mouse mat"]

#since lists are iterable, we can use a for loop to iterate through each item

for part in computer_parts: 
    print(part)

print()
#accessing list items by index
print(computer_parts[2]) #keyboard

#slicing lists to get a subset
print(computer_parts[:3]) #['computer', 'monitor', 'keyboard']
print(computer_parts[-1:]) #['mouse mat']
