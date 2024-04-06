def test1():
    print("Inside Test1 function and return")
    return
    # print("Inside Test1 function and after return")


def test2():
    print("Inside Test2 function and yield")
    yield
    print("Inside Test1 function and after yield")


test1()
print("test1 called")
test2()
print("test2 called")
