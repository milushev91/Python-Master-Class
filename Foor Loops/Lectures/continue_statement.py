shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shopping_list:
    #continue prevents the rest of the code in the loop from executing
    #it makes the loop jump to the next iteration
    if item == "spam":
        continue
    print("Buy " + item)
