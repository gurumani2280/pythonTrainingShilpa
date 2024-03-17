#To find the perimeter and area of rectangle
def perimeter(l,w):
    print("Enter length and width values : input - ", l,w)
    return 2*(l+w)

print(perimeter(4,5))
print()
l=int(input("Enter the length l:"))
w=int(input("Enter the width w:"))

print("The Perimeter of rectangle is : ", (perimeter(l,w)))

print()

print("AREA OF RECTANGLE")
def area(l,w):
    print("Enter length and width values : input - ", l,w)
    return l*w

print(area(6,4))
print()

l=int(input("Enter the length:"))
w=int(input("Enter the width:"))
print("The area of rectangle is : ", area(l,w))