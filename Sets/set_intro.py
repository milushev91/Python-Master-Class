
#creating set through literal
#sets are unordered and include only unique elements inside
#you can online put items inside sets which are hashable
# since sets are unordered you can't get item through index or slice it.
# Python won't allow this and will throw typeerror
farm_animals = {"cow", "sheep", "hen", "goat", "horse"} 
print(farm_animals)

for animal in farm_animals:
  print(animal)

# print(farm_animals[1])

more_animals = {"sheep", "goat", "hen", "cow", "horse"}

if farm_animals == more_animals:
  print("Sets are equal.")
else:
  print("Sets are different")
#Output : Sets are qual
#Python consider sets to be equal if they contain the same items

#creating sets through set() function
# You can pass any iterable to create set from
# When paired with `in` key word sets are more efficient then lists
# that is because when we are using it with list Python has check every
# every item from the first until it finds
# sets are using hashes like disctionaries and thus has fast ways of getting items

numbers = set("12345")
numbers2 = set(range(1, 6, 1))
print(numbers, numbers2)
