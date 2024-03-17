"""There are 4 types of actual arguments.
1.Positional Arguments or Required Arguments
2.Keyword Arguments or Named Arguments
3.Default Arguments
"""
import math

def GCD_check(x=5,y=3):
    print("Enter the no:s,input - ", x,y)
    return math.gcd(x,y)

print(GCD_check(20,40))
print(GCD_check())