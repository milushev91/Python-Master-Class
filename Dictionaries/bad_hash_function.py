data = [
    ("orange", "a sweet, orange, citrus fruit"),
    ("apple", "good for making cider"),
    ("lemon", "a sour, yellow citrus fruit"),
    ("grape", "a small, sweet fruit growing in bunches"),
    ("melon", "sweet and juicy"),
]

# returns ascii value of char
print(ord("a"))

def simple_hash(s: str) -> int:
    """
    Simple hashing function. Calculates has by modular devision
    of first char Ascii value by 10.
    
    :param s: Description
    :type s: String to be hashed
    :return: Hash as integer
    :rtype: int
    """

    basic_hash = ord(s[0]) % 10
    return basic_hash


def get(key: str) -> str:
    """Return a value for a key or None if key doesn't exist."""

    hash_code = simple_hash(key)

    if values[hash_code]:
        return values[hash_code]
    else:
        return None

# Python built in hash function vs our simple hash function
for key in data:
    print(hash(key), simple_hash(key[0]))

keys = [""] * 10
values = keys.copy()

for key, value in data:
    h = simple_hash(key)
    print(h)
    keys[h] = key
    values[h] = value

print(keys)
print(values)
print()

value = get("lemon")
print(value) # Output: a sour, yellow citrus fruit
