


def test2():
    print("Inside Test2 function and yield")
    yield 2
    print("Inside Test1 function and after yield")
    yield 3



y = test2()

for i in y:
    print(i)
print("test2 called")


"""
Inside Test2 function and yield
2
Inside Test1 function and after yield
3
test2 called
"""