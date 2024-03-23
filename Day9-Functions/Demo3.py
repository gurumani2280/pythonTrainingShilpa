#Write a function to check a given number is even or not.

def even_check(x):
    if x%2==0:
        print("The given number",x,"is an even number")
    else:
        print("The given number", x, "is an odd number")
even_check(21)
even_check(1)
even_check(2)
even_check(3)
even_check(78)
even_check(int(input("Pls enter a number:")))

