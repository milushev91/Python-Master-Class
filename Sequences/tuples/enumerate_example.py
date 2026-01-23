sequence = "abcdefg"

for index, value in enumerate(sequence):
    print(index, value)

#enumerate return tuple on each iteration, which can be unpacked
for t in enumerate(sequence):
    print(t)
    index, value = t
    print(index, value)

index, value = (0, 'a')
print(index, value) #0 a
