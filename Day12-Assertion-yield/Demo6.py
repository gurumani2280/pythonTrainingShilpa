


def test2():
    print("Inside Test2 function and yield")
    yield 2
    print("Inside Test1 function and after yield")



y = test2()
print(y) #<generator object test2 at 0x0000020408BB4DC0>
print(type(y)) #<class 'generator'>
for i in y:
    print(i)
print("test2 called")

"""
<generator object test2 at 0x0000020408BB4DC0>
<class 'generator'>
Inside Test2 function and yield
2
Inside Test1 function and after yield
test2 called
"""