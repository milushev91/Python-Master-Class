menu = [
    ["egg", "bacon", "spam"],
    ["egg", "tomato", "ham"],
    ["egg", "sausage", "spam"],
    ["egg", "spam", "spam", "spam"],
    ["ham", "bacon", "tomato"],
    ["egg", "bacon", "spam", "spam"]
]

for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(f"{item}")
    else:
        print(f"{meal} has spam count: {meal.count('spam')}")
