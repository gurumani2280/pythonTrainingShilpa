def sum1(n,*x):
    print("Inputs:",n,x)
    return n+sum(x)
print(sum1(5))
print(sum1(5,8))
print(sum1(5,8,9))

"""
Inputs: 5 ()
5
Inputs: 5 (8,)
13
Inputs: 5 (8, 9)
22
"""