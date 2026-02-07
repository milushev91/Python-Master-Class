from contents import pantry, recipes

display_dict = {}
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
 
        for item, required_quantity in ingredients:
            if item in pantry:
                available_quantity = pantry[item]

                if required_quantity > available_quantity:
                    print(f"You need {required_quantity - available_quantity} more {item}")
                else:
                    print(f"{item} is OK")

            else:
                print(f"{item} is NOK")
