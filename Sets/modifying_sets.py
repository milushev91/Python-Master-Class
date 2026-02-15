# creating empty set
# you cannot use the code from the line bellow because it will create empty dictionary
#numbers = {}

# to create empty set you can use {} and inside them you can unpack with * other empty
#sequence like string, tuple, dictionary, list, etc
# It is advisable to use that approach only if performance is most important
# since it is less semantic and other programmer could spent more time to 
# understand it

numbers = {*{}}
print(numbers, type(numbers)) # {}, class set

# more readable way of creating empty set
numbers2 = set()

#add method adds hashble item to set
# if value is already inside, it won't be added, no error is rised
numbers2.add(1)
print(numbers2) # {1}
numbers2.add(1)

while len(numbers2) < 4:
  new_number = int(input("Please enter your new value: "))
  numbers2.add(new_number)

print(numbers2) # {1, 2, 3, 4}

data = [ "red", "blue", "red", "blue", "green", "white"]

#creating alphabeticaly ordered list and removing duplicates.
#Since using set() order is not preserved
unique_data = sorted(set(data))

# to preserve order you can after 3.6 version you can use dict.fromkeys()
# it will convert the list into dictionary with unique keys, keeping the order
# from the list with None as value
# the list function will create list of the keys, again keeping the order
unique_data_2 = list(dict.fromkeys(data))
print(unique_data_2)

