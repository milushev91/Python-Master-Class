# hashlib is a module that provides a common interface to many
#  different secure hash and message digest algorithms.
import hashlib


#.algorithms_guaranteed is a set of algorithms that are
#  guaranteed to be supported by the hashlib module on all platforms.
print(sorted(hashlib.algorithms_guaranteed))
#.algorithms_available is a set of algorithms that are available in
#  the current Python environment. This may include additional
#  algorithms that are not guaranteed to be available on all platforms.
print(sorted(hashlib.algorithms_available))

python_program = """for i in range(10):
    print(i)"""

print(python_program)

#.encode() method is used to convert a string into bytes. 
# The argument "utf-8" specifies the encoding to use.
# In this case, it converts the string into a sequence of bytes 
# using the UTF-8 encoding.
for b in python_program.encode("utf-8"):
    print(b, chr(b))

# hashlib.sha256() creates a new sha256 hash object.
# The argument is the data to be hashed, which must be in bytes.
# The resulting hash object can be used to compute the hash of the data.
original_hash = hashlib.sha256(python_program.encode("utf-8"))

#.hexdigest() method returns the hash value as a hexadecimal string.
print(f"SHA256 hash of the original program: {original_hash.hexdigest()}")

python_program += "\nprint('New code added')"

new_hash = hashlib.sha256(python_program.encode("utf-8"))
print(f"SHA256 hash of the modified program: {new_hash.hexdigest()}")

if new_hash.hexdigest() == original_hash.hexdigest():
    print("The program has not been modified.")
else:
    print("The program has been modified.")
