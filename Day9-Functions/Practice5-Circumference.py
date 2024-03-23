#To find the circumference of the circle taking radius as input
def circum(r):
    print("Enter the radius - input:", r)
    PI=3.14
    return 2*PI*r

print("The circumference is :",circum(9))
print()

r=int(input("Enter the radius:"))
print("The circumference is :",circum(r))
