#multiple assignment
a = b = c = d = e = f = 12
print(a, b, c, d, e, f)  # 12 12 12 12 12 12

#unpacking a tuple
x, y, z = 1, 2, 76
print(x)  # 3
print(y)  # 2
print(z)  # 76

print("Unpacking a tuple: ")

data = 1, 2, 76
x, y, z = data
print(x)  # 1
print(y)  # 2
print(z)  # 76

print("Unpacking a list: ")

# you can unpack any sequence typ

data_list = [1, 2, 76]
data_list.append(15)
#line below will raise ValueError: too many values to unpack (expected 3)
#this problem isn't present when unpacking tuples
#because you always know the length of the tuple and they are immutable
p, q, r = data_list
print(p) #1
print(q) #2
print(r) #76

