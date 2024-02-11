#Finding minimum of 3 inputs using nested ternary operator

x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=int(input("Enter 3rd number:"))
min=x if x<y and x<z else y if y<z else z
print("Minimum", min)