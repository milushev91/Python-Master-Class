data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# when using print function it calls the __str__ method
# which returns the string representation of the object
# and thus you do not have to covert other data types to string
# If you are using write() first you have to convert non-string types
# to string since you can only save strings to files.
plants_filename = "plants_filename.txt"

with open(plants_filename, "w") as plants:
    for plant in data:
        plants.write(plant)

