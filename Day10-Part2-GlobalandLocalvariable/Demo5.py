#Write a prgm to print fibonacci series upto n number using recusrion.
# input as 6 then this o/p > 0,1,1,2,3,5,8...

def fibonacci(n):
    if n==0 or n==1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#print(fibonacci(0))
#print(fibonacci(1))
#print(fibonacci(6))

n=int(input("Pls enter a number to be calculated to print the fibonacci series:"))
for i in range(0,n+1):
    print(fibonacci(i), end=" ")