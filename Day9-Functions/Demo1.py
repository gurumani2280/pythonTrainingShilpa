def greeting():
    print("hello from greetings")
greeting()
greeting()
print(greeting()) #Calling greeting() and returned value is printed to console
y=greeting() #Calling greeting() and storing returned value to y.
print(y)

#Function : A group of statements that can be called any number of times.
#We define function for reusability(we can call the function any no.of times).
#Reusability means to avoid code redundancy.

# Two types of function:
#1.Build In Function : Ex-Print,input,eval,len,id
#2.User Defined function: Functions created by programmer using def keyword.


def add(a,b):
    print("Inside add function:-input",a,b)
    return a+b
add(5,6) #Returned value of add(), we are not utilising here.
print(add(5,6)) #Returned value of add(), we are  utilising to print on console.
x=add(9,16) #returned value of add() is utilised to store in x.
print(x)

#return keyword is also used while creating function to return some value.return is optional, not mandatory.
#if return statement is not there,then it retuns None.