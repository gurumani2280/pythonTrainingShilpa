#To calculate factorial of a no: using recursion
def fact(n):
    if n==1: #This is the base condition or termination condition
        return 1
    else:
        return n*fact(n-1) #calling function itself


print(fact(1))
print(fact(2))
print(fact(3))
print(fact(4))


