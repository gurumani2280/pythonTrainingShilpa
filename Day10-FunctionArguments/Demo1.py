"""There are 5 types of actual arguments.
1.Positional Arguments or Required Arguments
2.Keyword Arguments or Named Arguments
"""
def max_check(x,y):
    print("Input is:", x,y)
    if x>y:
        print("Maximum",x)
    else:
        print("Maximum",y)


max_check(9,99)
print()
max_check(x=5,y=9)
max_check(y=10,x=9)
