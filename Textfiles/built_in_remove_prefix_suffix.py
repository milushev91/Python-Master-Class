with open("jabberwocky.txt") as jabber:
  #'Twas brillig, and the slithy toves
  first = jabber.readline().rstrip()

# removeprefix() removes the prefix from the string
# prefix is the string to be removed from the beginning of the string
twas_removed = first.removeprefix("'Twas")
print(twas_removed) # brillig, and the slithy toves

# removesuffix() removes the suffix from the string
# suffix is the string to be removed from the end of the string
toves_removed = first.removesuffix("toves")
print(toves_removed) #'Twas brillig, and the slithy 
