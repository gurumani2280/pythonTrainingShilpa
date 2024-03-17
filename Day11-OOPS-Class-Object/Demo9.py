
class Employee:

    def __init__(self):
        self.name="Ram"
        print("The name of employee inside constructor is:", self.name)






myobj1=Employee()
print("Name of the employee for myobj1:",myobj1.name)
myobj1.age=50
print("Age of the employee for myobj1 :",myobj1.age)
"""
Output:
The name of employee inside constructor is: Ram
Name of the employee for myobj1: Ram
Age of the employee for myobj1 : 50

"""
