#Program to find sum of n numbers
x=int(input("Enter a number:"))
sum=0
y=1
while y<=x:
    sum += y
    y=y+1
print("Sum", sum)
print("Using Formula", (x*(x+1))//2)
