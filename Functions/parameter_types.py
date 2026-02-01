def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional-(*args):..{}".format(*args))
    print("keyword..................{}".format(k))
    print("var-keyword-(*kwargs)....{}".format(kwargs))

print(1, 2, 3, 4, 5, k=6, k1=7, k2=8)
