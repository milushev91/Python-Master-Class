# creating a tuple
# they could be created without () but there cases where () are required
# in order not to remember them you could simply always
t = ("a", "b", "c")

print(t) # ("a", "b", "c")

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budjiet = "Budgie", "Budgie", 1971
imelda = "Imelda May", "Imelda May", 2011
metallica = "Metallica", "Metallica", 1993

print(welcome) # ('Welcome to my Nightmare', 'Alice Cooper', 1975
#indexes works the same way as lists and strings
print(welcome[0]) # Welcome to my Nightmare

#unlike lists tuples are immutable
# welcome[0] = "Welcome to my Nightmare - Remastered" # this will raise an error

metallica2 = list(metallica) # converting tuple to list
metallica2[0] = "Metallica - Remastered"
