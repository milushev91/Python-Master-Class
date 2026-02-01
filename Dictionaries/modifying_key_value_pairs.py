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
    #if dictionary two or more same keys, the previous are replaced with the last one
    "PB7606HB": "Ford Primal",
    "PB7609HB": "Opel Astra",

}

# changing key value
vehicles["PB7609HB"] = "Opel Vectra"
print(vehicles["PB7609HB"] ) # Opel Vectra

print(vehicles["PB7606HB"]) # Ford Primal

for key, value in vehicles.items():
    print(key, value, sep=": ") # no "PB7606HB": "Ford Focus" pair, it is replaced by
    #"PB7606HB": "Ford Focus" by "PB7606HB": Ford Primal, which is the last
