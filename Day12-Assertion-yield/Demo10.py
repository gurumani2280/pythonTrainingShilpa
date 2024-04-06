
def test2():
    print("Inside Test2 function and yield")
    yield 2
    print("Inside Test1 function and after yield")
    yield 3



y = test2()
print(next(y))
print("First yield completed")
print(next(y))
print("Second yield completed")
# print(next(y))



"""
Function created w/o using "yield" keyword is regular function.
Function created using "yield" keyword is generator function.yield can be used multiple times and depends upon the no.of times yield is used, that many times 
next method can be called on generator function.
If we are calling next method extra than the yield, then we will get "StopIteration" :exception
Better to use for loop or convert to list to avoid "StopIteration" exception.

yield saves the state of the function,"next" time function is called, execution continues from where its left off,With same variable value,it had before yielding
whereas return terminates the function completely
Another diff is that generator functions dont even run a function, it oly creates and return generator object
Lastly,code in generator function only executes when next is called on generator object.



O/P:
Traceback (most recent call last):
  
    print(next(y))
          ^^^^^^^
StopIteration
Inside Test2 function and yield
2
Inside Test1 function and after yield
3

"""
