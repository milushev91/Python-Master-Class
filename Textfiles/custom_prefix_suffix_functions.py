def removeprefix(string, prefix):
  if string.startswith(prefix):
    return string[len(prefix)::]
  return string
  
def removesuffix(string, suffix):
  if string.endswith(suffix):
    return string[:len(string) - len(suffix)]
  return string


with open("jabberwocky.txt") as jabber:
  #'Twas brillig, and the slithy toves
  first = jabber.readline().rstrip()

twas_removed = removeprefix(first, "'Twas")
print(twas_removed) #  brillig, and the slithy toves

toves_removed = removesuffix(first, "toves")
print(toves_removed) # 'Twas brillig, and the slithy 

