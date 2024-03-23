#To find the maximum of 2 given no:s
def max_check(x,y):
    print("Input is:", x,y)
    if x>y:
        print("Maximum",x)
    else:
        print("Maximum",y)


max_check(9,99)
print()
x=(int(input("Pls enter a number:")))
y=(int(input("Pls enter 2nd number:")))
max_check(x,y)

