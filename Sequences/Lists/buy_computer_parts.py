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
        choisen_option = options[int(current_choice) - 1]

        if choisen_option in computer_parts:
            print("Removing " + choisen_option)
            #remove method removes the first occurrence of a value from a list
            #if the value is not found, it raises a ValueError
            computer_parts.remove(choisen_option)
        else:
            print(f"Adding {current_choice}")
            computer_parts.append(choisen_option) 

        print(f"Your computer parts are now: {computer_parts}")
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
