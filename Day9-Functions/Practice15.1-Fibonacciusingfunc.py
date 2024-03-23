#To find out nth fibonacci no:
def fibonacci_series(n):
    num1 = 0
    num2 = 1
    count = 0
    while count<=n:
        print(num1)
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        count = count + 1

n=int(input("Pls enter a number to get the fibonacci series: "))
fibonacci_series(n)
