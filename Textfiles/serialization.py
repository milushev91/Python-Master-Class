# serialization is when  you convert data into a format that can be stored or transmitted
# and then later reconstructed back into the original data format.

import json

languages = [
    ['ABC', 1987],
    ['Algol 68', 1968],
    ['APL', 1962],
    ['C', 1973],
    ['Haskell', 1990],
    ['Lisp', 1958],
    ['Modula-2', 1977],
    ['Perl', 1987],
]

# Serializing json
with open("test.json", "w", encoding="utf-8") as test_file:
  # dump() converts a Python object into a JSON string and writes it to a file.
  json.dump(languages, test_file)

# Deserializing json
with open("./test.json", "r", encoding="utf-8") as test_file:
   # load() reads a JSON string from a file and converts it back into a Python object.
   data = json.load(test_file)  

print(data)
print(data[2])

