x_sum = 0 #This is a global variable which is defined outside the function and can be accessed within anywhere in the file
def add_odd(n): #n is a local variable defined inside a function and can be accessed only inside this function.
    print("Input is:",n)
    global x_sum
    print("Initial input is :", x_sum)
    for i in range(1,n):

        if (i%2!=0):
            print(i)
            x_sum = x_sum+i 
            i = i+1
    print("The Final output is :",x_sum)


#print(n) #NameError: name 'n' is not defined
#add_odd(5)
print(x_sum)