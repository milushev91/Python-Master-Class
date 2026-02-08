from contents import recipes

def my_deepcopy(d: dict) -> dict:
    """
    Creates one level deepcopy of dictionary.
    
    :param d: Dictionary to be deepcopied.
    :type d: dict
    :return: Deepcopy of the d in a new dictionary
    :rtype: dict
    """
    new_d = {}

    for key, value in d.items():
        new_d[key] = value.copy()
    
    return new_d

recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300

print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
