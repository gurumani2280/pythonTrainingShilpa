"""
Classes are logical collection of attributes/properties(variables) and methods(action/behavior)
Properties can be represented by variable
Actions can be represented by method
Hence a class can have variables and methods

There are 2types of variables allowed inside a class.
1.Static variables (class level variables)
2.Instance variables (object level variables)

Static variables can be accessed using classname,also with reference variables.
Whatever variable created inside a class directly is a static/class variable.
Static/Class variable is common to all the objects.
self is a reference variable which will point to current object.
For all the instance method,self  should be the first argument/parameter

How to create instance variable ?
Using reference variable,if you create any variable then it will be instance variable.
Instance variable value could be specific for each object

How to access instance variable?
We can access using reference or self variable
Inside a class,we can have 3 types of methods:
1.Static Method - For all the static method, self or cls is not there.
2.Class Method - For all the class method,cls should  be the first argument/parameter
3.Instance Method - For all the instance method,self should be the first argument/parameter
"""

class Employee:
    company_name="ABC"
    def __init__(self):
        print("This method will be executed when ever object of class employee is created")
        print("Company name of myobj1:", self.company_name)
        self.name="Ram"
        print("The name of employee is:", self.name)


print("Name of the company:", Employee.company_name)

myobj1=Employee() #This method will be executed when ever object of class employee is created
print("Company name of myobj1:", myobj1.company_name)
print("Name of the employee:",myobj1.name)
myobj2=Employee() #This method will be executed when ever object of class employee is created
print("Company name of myobj2:", myobj2.company_name)
print("Name of the employee:",myobj2.name)

