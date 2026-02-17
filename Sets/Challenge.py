text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here
words_list = text.split()
preps_used = prepositions.intersection(words_list)
print(preps_used)
