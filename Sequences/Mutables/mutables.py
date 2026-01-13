shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

another_list = shopping_list
print(id(shopping_list)) # Memory address of shopping_list
print(id(another_list))  # Same memory address as shopping_list

# The += operator adsds items to the existing list in place
shopping_list += ["cookies"]
#New items are added to the original list, and no new list is created
print(shopping_list)  # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']
print(id(shopping_list)) # Same memory address as before
print(id(another_list))  # Same memory address as before

print(another_list)  # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']

a = b = c = d = e = f = another_list

print(a) # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies']

print("Adding cream")
b.append("cream")

print(c) # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies', 'cream']
print(d) # ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice', 'cookies', 'cream']
