#To calculate factorial of a no:

import math
def fact(n):
    print("Enter the number to find the factorial - input:", n)
    return math.factorial(n)

print(fact(4))
n=int(input("Enter the number:"))
print("The factorial of given number is:",fact(n))



