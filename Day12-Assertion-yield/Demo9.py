


def test2():
    print("Inside Test2 function and yield")
    yield 2
    print("Inside Test1 function and after yield")
    yield 3



y = test2()
print("list of y", list(y))