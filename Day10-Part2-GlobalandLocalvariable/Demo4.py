"""Take an input number. Say 10 and print 10 to 0 using recursion.
o/p :  10 9 8....0
In recursion, we have a base condition or a termination condition and
second thing in recursion is calling function itself with reduced input
"""

def print_till_zero(n):
    print(n,end=" ")
    if n==0:
        return
    else:
        print_till_zero(n-1)

print_till_zero(0)
print()
print_till_zero(6)