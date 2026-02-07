from contents import pantry

# setdefault() method of dict is used to get the value of a key if it is in the dict,
chicken = pantry.setdefault("chicken", 0)
print(chicken) # Output: 500

# if the key is not in the dict, it will set the key to the default value (0 in this case)
#  and return it.
beans = pantry.setdefault("beans", 0)
print(beans) # Output: 0

ketcthup = pantry.get("ketchup", 0)
print(ketcthup) # Output: 0

# if we use get() method, it will return None if the key is not in the dict,
# unless we specify a default value (0 in this case).
# but unlike setdefault(), it will not add the key to the dict.
for key, value in pantry.items():
    print(f"{key}: {value}")
