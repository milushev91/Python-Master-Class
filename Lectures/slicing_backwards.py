#Slicing backwards

letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:: -1]
print(backwards)  #zyxwvutsrqponmlkjihgfedcba

another_backwards = letters[::-1]
print(another_backwards)  #zyxwvutsrqponmlkjihgfedcba

#Challanges: 
#1. slice substring qpo

print(letters[-10:13:-1])

#2. edcba

print(letters[-22::-1])

#3. last 8 in reverse order
print(letters[:-9:-1])

#return last n characters
print(letters[-4:])  #wxyz
#get last character
print(letters[-1:])   #z
#get first character
print(letters[:1])    #a
#last two are useful because they won't raise an error if the string is empty
