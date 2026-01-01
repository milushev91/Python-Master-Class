activity = input("What would you like to do today? ")

# not in operator is used to check if a value does not exist in a sequence
# behind the scenes, it is doing something like this:
# found = False
# for item in activity:
#     if item == "cinema":
#         found = True
#         break
# if not found:
#     print("But I want to go to the cinema!")
#casefold() is used to make the check case-insensitive
#it converts all characters to lowercase
#it is similar to lower() but more aggressive
# for example, it converts the German letter 'ß' to 'ss'
# this helps in making accurate comparisons
if "cinema" not in activity.casefold():
    print("But I want to go to the cinema!")
