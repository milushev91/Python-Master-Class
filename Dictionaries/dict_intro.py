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

# get value out of a dict with key through []
my_car = vehicles["PB7608HB"]
print(my_car) #Mazda 2

# get value out of a dict with key get method
mazda_3 = vehicles.get("PB7602HB")
print(mazda_3) #Mazda 3
