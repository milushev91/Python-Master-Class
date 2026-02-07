from contents import pantry, recipes

def add_item(item: str, quantity: int, dict: dict) -> None:

    """
    Adds item and quantity to a dict as key-value pair. If item already
    in it, it will increase its value by the quantity amount.
    
    :param item: Key name
    :type item: str
    :param quantity: Amount to add
    :type quantity: int
    :param dict: The dictionary that will store the pair.
    :type dict: dict

    :return: None
    """

    # if item not in dict:
    #     dict[item] = 0
    
    # dict[item] += quantity
    # the above code can be simplified by using setdefault() method of dict
    # setdefault() will return the value of the key if it is in the dict, 
    # otherwise it will set the key to the default value (0 in this case) and return it.
    dict[item] = dict.setdefault(item, 0) + quantity

display_dict = {}
items_to_buy = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    print("Please choose your recipe: ")
    print("-" * 25)

    for key, value in display_dict.items():
        print(f"{key}: {value}")
    
    choice = input("> ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients...")
        ingredients = recipes[selected_item]
    
 
        for item, required_quantity in ingredients.items():
            if item in pantry:
                available_quantity = pantry[item]

                if required_quantity > available_quantity:
                    needed_quantity = required_quantity - available_quantity
                    print(f"You need {needed_quantity} more {item}")
                    add_item(item=item, quantity=needed_quantity, dict=items_to_buy)
                else:
                    print(f"{item} is OK")

            else:
                print(f"{item} is not found in your pantry. Please buy.")
                add_item(item=item, quantity=needed_quantity, dict=items_to_buy)

