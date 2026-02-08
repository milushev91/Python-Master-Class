import copy

nested_dict = {
    "items": [1, 2, 3, 4, 5],
    "key": "value"
}

nested_dict_deep_copy = copy.deepcopy(nested_dict)
nested_dict["items"].append(6)
print(nested_dict_deep_copy["items"]) # [1, 2, 3, 4, 5]
