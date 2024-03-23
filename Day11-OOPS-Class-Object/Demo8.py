
class Employee:

    def __init__(self):
        self.name="Ram"
        print("The name of employee inside constructor is:", self.name)
        #print("Name1 of the employee inside constructor:", myobj1.name1) #NameError: name 'myobj1' is not defined





myobj1=Employee()
print("Name of the employee for myobj1:",myobj1.name)
myobj1.name1="Raj"
print("Name1 of the employee for myobj1 :",myobj1.name1)

"""
Output:
The name of employee inside constructor is: Ram
Name of the employee for myobj1: Ram
Name1 of the employee for myobj1 : Raj

"""