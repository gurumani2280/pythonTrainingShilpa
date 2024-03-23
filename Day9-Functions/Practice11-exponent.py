#Take  two user inputs and find the exponent

def exp_check(x,y):
    print("Enter the numbers to get the exponent-input:",x,y)
    return x**y

print(exp_check(2,2))

x=int(input("Enter the first number:"))
y=int(input("Enter the second number:"))
print("The exponent of the numbers is : ", exp_check(x,y))