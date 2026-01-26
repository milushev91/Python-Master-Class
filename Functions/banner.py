#functions can use parameters and you can set them a default value
def banner_text(text=" ", screen_width=80):

    if len(text) > screen_width - 4:
        raise ValueError("String '{0}' is larger than specified width {1}".format(text, screen_width - 4))

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)

#if you give a an argument to the function, it will override the default value
banner_text("*", 80)
#also when you have a default value you can omit the argument when calling the function
#it will use the default value instead
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,", 80)
banner_text("There's something you've forgotten!", 80)
banner_text("And that's to laugh and smile and dance and sing,", 80)
#keyword arguments allow you to specify only certain parameters
#you can also use keyword arguments to change the order of parameters
#here we are using the default value for text and specifying a value for screen_width
banner_text(screen_width=80)
banner_text("When you're feeling in the dumps,", 80)
banner_text("Don't be silly chumps,", 80)
banner_text("Just purse your lips and whistle - that's the thing!", 80)
banner_text("And... always look on the bright side of life...", 80)
banner_text("*", 80)
#in python, functions that do not explicitly return a value will return None by default
result = banner_text("Nothing is returned", 80)
print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())
