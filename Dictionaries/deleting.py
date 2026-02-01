
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

#deleting key from a dictionary
del vehicles["PB7602HB"]

print(vehicles) # No "PB7602HB" key

# if the key is not in the dictionary raises keyError
# del vehicles["f1"]

#using pop method
opel_Astra = vehicles.pop("PB7609HB")
print(vehicles) # Opel Astra
#raises KeyError if key not in dictionary
# opel_Astra = vehicles.pop("PB7609HB")

#to not crash the program you can set a default return value if key is not
#in the dictionary
opel_Astra = vehicles.pop("PB7609HB", "Car with that registration not available")
print(opel_Astra)
