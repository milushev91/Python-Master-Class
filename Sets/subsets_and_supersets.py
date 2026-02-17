morning = {"Java", "C", "Ruby", "Lisp", "C#"}
afternoon = {"Python", "C#", "Java", "C", "Ruby"}

# symethric difference
# ^ operator returns only the unique items from both sets
# this means only items which are present in one set and not in the other
# in the example below Python, Lisp will be in the new set since Python is only present
# in the second set and Lisp only in the first
possible_courses = morning ^ afternoon
print(possible_courses)

# method two using: lists and symmetric_difference method
morning_list = ["Java", "C", "Ruby", "Lisp", "C#"]
afternoon_list = ["Python", "C#", "Java", "C", "Ruby"]

possible_courses_2 = set(morning_list).symmetric_difference(afternoon_list)

print(possible_courses_2)
