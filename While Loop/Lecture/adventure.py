available_exits = ["north", "south", "east", "west"]

chosen_exit = input("Please choose valid direction: ")

while chosen_exit not in available_exits:
    chosen_exit = input("Please choose valid direction: ")

    if chosen_exit == "quit":
        print("Game over!")
        #break does the same thing with while loop as for loop
        #it stops the loop
        break

print("aren't you glad you got out of there")
