menu = [
    ["egg", "bacon", "spam"],
    ["egg", "tomato", "ham"],
    ["egg", "sausage", "spam"],
    ["egg", "spam", "spam", "spam"],
    ["ham", "bacon", "tomato"],
    ["egg", "bacon", "spam", "spam"],
    ["egg", "bacon", "tomato", "spam"],
    ["spam", "bacon", "tomato", "spam"],
]

#printing solution

# for meal in menu:
#     line = "[ "

#     for item in meal:
#         if item != "spam":
#             line += item + ", "
#     line += "]"  
#     print(line)

#modifying list

for meal in menu:
    while "spam" in meal:
        meal.remove("spam")
    print(meal)
