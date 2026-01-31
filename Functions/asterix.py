numbers = (1, 2, 3, 4, 5)

print(numbers, sep=":")
#unpacking 
print(*numbers, sep=";")
print(1, 2, 3, 4, 5, sep=";")

def test_star(*args):
    # args is a tuple
    print(args)
    for x in args:
        print(x)

#We can pass as many arguments as want or no arguments as args
test_star(0, 1, 2, 3, 4, 5)
