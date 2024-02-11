
#Using Ternary Operator - Find max and min of 2 user inputs.
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
min=x if x<y else y
print("Minimum", min)

max=x if x>y else y
print("Maximum", max)