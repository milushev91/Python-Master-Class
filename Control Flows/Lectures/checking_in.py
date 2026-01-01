parrot = "Norwegian Blue"
letter = input("Enter a letter: ")

#in operator is used to check if a value exists in a sequence
#behind the scenes, it is doing something like this:
# found = False
# for char in parrot:
#     if char == letter:
#         found = True
#         break
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")
