farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

#.union() creates a new set from all unique items from two sets
# it doesn't matter on which set the method is called
all_animals = farm_animals.union(wild_animals)
# `|` operator does the same thing as union()
all_animals2 = farm_animals | wild_animals

print("-" * 50)

from prescription_data import adverse_interactions

meds_to_watch = set()

for interaction in adverse_interactions:
  # ways of create new set from the unique items of two other sets
  #meds_to_watch = meds_to_watch.union(interaction)
  #meds_to_watch = meds_to_watch | interaction

  #updating the items of existing set by adding items from the passed set 
  #meds_to_watch.update(interaction)
  #operator to do the update
  meds_to_watch |= interaction

#another way
#set methods have several advantages over operators
#1st they can recieve any iterable as argument, unlike operators which can be used
#only with sets
#2nd they can recieve more than one argument
#they code bellow removes the need for the for loop and the update on each operation
meds_to_watch.update(*adverse_interactions)
  
