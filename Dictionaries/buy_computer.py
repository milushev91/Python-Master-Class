def print_options(options: dict) -> None:
    """
    Docstring for print_options
    
    :param options: Description
    :type options: dict
    """
    print("Please choose from the options bellow (0 to exit): ")

    for key, value in options.items():
        print(f"\t{key} : {value}")


parts_options = {"1": "computer", 
           "2": "monitor", 
           "3": "keyboard", 
           "4": "mouse", 
           "5": "mouse mat", 
           "6": "hdmi cable"
           }

computer_parts = []

print_options(options=parts_options)

choice = input("> ")

while choice != "0":

    if choice not in parts_options:
        print("invalid choice")
        print_options(options=parts_options)
    else:
        item = parts_options[choice]
        if item not in computer_parts:
            print(f"Adding: {item}")
            computer_parts.append(item)
        else:
            print(f"Removing: {item}")
            computer_parts.remove(item)
        print(computer_parts)
    
    choice = input("> ")
else:
    print("Exited the program!")
