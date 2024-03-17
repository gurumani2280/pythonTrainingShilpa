#To find the perimeter and area of triangle
def perimeter(a,b,c):
    print("Enter a,b,c values : input - ", a,b,c)
    return a+b+c

print(perimeter(4,5,6))
print()
a=int(input("Enter the side a:"))
b=int(input("Enter the side b:"))
c=int(input("Enter the side c:"))
print("The Perimeter of triangle is : ", (perimeter(a,b,c)))

print()

def area(b,h):
    print("Enter breadth and height values : input - ", b,h)
    return (b*h)//2

print(area(6,4))
print()

b=int(input("Enter the breadth:"))
h=int(input("Enter the height:"))
print("The area of triangle is : ", area(b,h))


