#Write a function which takes one input number from the user and then return the square of the input no.

def square(x):
    return x**2
#square() #TypeError: square() missing 1 required positional argument: 'x'
square(9)
print(9,square(9))


#While calling a function, we should use function name and in circular bracket we have to provide matching argument.
#If argument is not matched,then we will get error. (Type error)
