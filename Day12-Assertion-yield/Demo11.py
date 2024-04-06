def test2():
    print("Inside Test2 function and yield")
    yield
    print("Inside Test2 function and yield")
    yield
    print("Inside Test2 function and yield")
    yield
    print("Inside Test2 function and yield")
    yield




y = test2() #Its not calling test2() function. Its just returning generator object and storing in y.

for i in y:
    pass
print("test2 called")
next(y) #StopIteration


"""

Inside Test2 function and yield
Inside Test2 function and yield
Inside Test2 function and yield
Inside Test2 function and yield
test2 called
StopIteration -- #line 19
"""