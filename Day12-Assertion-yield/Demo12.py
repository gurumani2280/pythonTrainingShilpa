def gen_func(x):
    for i in range(x):
        yield i

print(list(gen_func(5)))
x=range(5)
print(x)
print(type(x))
print(list(range(5)))