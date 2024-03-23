
class Employee:

    def __init__(self,local_name):
        self.name=local_name
        print("The name of employee inside constructor is:", self.name)






#myobj1=Employee() #TypeError: Employee.__init__() missing 1 required positional argument: 'local_name'
myobj1=Employee("Roshan")
print("Name of the employee for myobj1:",myobj1.name)
myobj1.age=50
print("Age of the employee for myobj1 :",myobj1.age)
myobj2=Employee("Reena")
print("Name of the employee for myobj2:",myobj2.name)
myobj3=Employee("John")
print("Name of the employee for myobj3:",myobj3.name)

"""
Output : 
The name of employee inside constructor is: Roshan
Name of the employee for myobj1: Roshan
Age of the employee for myobj1 : 50
The name of employee inside constructor is: Reena
Name of the employee for myobj2: Reena
The name of employee inside constructor is: John
Name of the employee for myobj3: John
"""


