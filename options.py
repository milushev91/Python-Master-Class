options = ["1. Learn Python", "2. Learn Math", "3. Learn Computer Science", "4. Learn Machine Learnig", "5. Learn Deep Learning", "0. Exit"]
options_string = ""

for option in options:
    options_string += "\t" + option + "\n"

answer = input(f"Please chose an option from the list bellow: \n{options_string}")

while answer != "0":

    if answer in "12345":
        print(f"You chosen option: {options[int(answer) - 1]}")
    else:
        print("Invalid choice. Try again!")
    
    answer = input(f"Please chose an option from the list bellow: \n{options_string}")
else:
    print("You have exited the program!")


