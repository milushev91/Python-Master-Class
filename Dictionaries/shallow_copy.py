animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

things = animals # things will now point at same place in memmory
animals["teddy"] = "toy" # the following change will be applied in
# the things dict too
print(things["teddy"]) # toy

# copy creates a shallow copy from the animals dict
# it will create new dict from animal things
# however shallow means that if there is a mutable object inside
# the dict it will point at the same place in memory as
# the mutable object the dict we are copping
another_things = animals.copy()
animals["cat"] = "cute"

print(another_things) # no cat: cute pair inside another things

nested_dict = {
    "items": [1, 2, 3, 4, 5],
    "key": "value"
}

nested_dict_shallow_coppy = nested_dict.copy()
nested_dict["another key"] = "another value"

print(nested_dict_shallow_coppy) # no another key
nested_dict["items"].append(6)
print(nested_dict_shallow_coppy["items"]) # [1, 2, 3, 4, 5, 6]
