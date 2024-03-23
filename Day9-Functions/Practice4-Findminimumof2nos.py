#To find the minimum of 2 given no:s
def min_check(x,y):
    print("Input is:", x,y)
    if x>y:
        print("Minimum",y)
    else:
        print("Minimum",x)


min_check(9,99)

x=(int(input("Pls enter a number:")))
y=(int(input("Pls enter 2nd number:")))
min_check(x,y)