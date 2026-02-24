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

flowers_filename = "flowers_name.txt"

# opens file to write in
with open(flowers_filename, "w") as plants:
    # loop through data
    for plant in data:
        # print plant line from data inside flowers_name.txt
        # by specifiying the file name in file argument
        print(plant, file=plants)
        
with open(flowers_filename) as plants:
    for plant in plants:
        print(plant.rstrip())

