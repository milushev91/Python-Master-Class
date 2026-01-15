options = ["computer", 
           "monitor", 
           "keyboard", 
           "mouse", 
           "mouse mat", 
           "hdmi cable"]
options_length = len(options)
current_choice = "-"
computer_parts = []
valid_choices = ""

for number in range(1, options_length + 1):
    valid_choices += str(number)
print(valid_choices)

while current_choice != "0":
    if current_choice in valid_choices:
        print(f"Adding {current_choice}")
        computer_parts.append(options[int(current_choice) - 1]) 
    else:
        print("Please choose from the following options:")
        # for i in range(options_length):
        #     print(f"{i + 1}: {options[i]}")
        #enumerate function returns both the index and the value of each item in the list
        #it is often used in loops when you need to keep track of the index of the current item
        for number, option in enumerate(options):
            print(f"{number + 1}: {option}")
        print("0: Exit")

    current_choice = input()

print(computer_parts)
