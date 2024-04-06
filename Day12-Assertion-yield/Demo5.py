def test1():
    print("Inside Test1 function and return")
    return 1
    # print("Inside Test1 function and after return")


def test2():
    print("Inside Test2 function and yield")
    yield 2
    print("Inside Test1 function and after yield")


x = test1()
print(x)
print(type(x))
print("test1 called")
y = test2()
print(y)
print(type(y))
for i in y:
    print(i)
print("test2 called")

"""
Inside Test1 function and return
1
<class 'int'>
test1 called
<generator object test2 at 0x0000029D461C4DC0>
<class 'generator'>
Inside Test2 function and yield
2
Inside Test1 function and after yield
test2 called
"""