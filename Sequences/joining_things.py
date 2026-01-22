flowers = [
    "Daffodil", "Tulip", "Rose", "Tiger Lily",
    "Sunflower", "Daisy", "Lavender", "Orchid",
    "Marigold", "Jasmine"
]

for flower in flowers:
    print(flower)

separtor = " | "    
#.join() is a string method that joins elements of a list into a single string
# using the string as a separator between elements.
# it is called on the string that will be used as a separator
# and takes the list as an argument.
# items inside must be strings otherwise it will raise an error.
output = separtor.join(flowers)
print(output)
