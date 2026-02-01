# creating dictionary with literals
# dictionaries include key-value pairs
vehicles = {
    "PB7608HB": "Mazda 2",
    "PB7602HB": "Mazda 3",
    "PB7604HB": "Mazda 5",
    "PB7603HB": "Mazda 6",
    "PB7605HB": "Ford Escort",
    "PB7607HB": "Ford Fiesta",
    "PB7606HB": "Ford Focus",
    "PB7609HB": "Opel Astra",
}

#iterating over dictionary
# getting key and value through for loop
for key in vehicles:
    print(key, vehicles[key], sep=": ")

print("-" * 80)

# more effecient approach using .items() method
for key, value in vehicles.items():
    print(key, value, sep=" ")
