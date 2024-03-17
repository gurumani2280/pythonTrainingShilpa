#To find out nth fibonacci no:

n=int(input("Pls enter a number to get the fibonacci series: "))
num1=0
num2=1
count=0
print("The fibonacci series for the given no is :")
while count<=n:
    print(num1)
    num3 = num1 + num2
    num1=num2
    num2=num3
    count=count+1








