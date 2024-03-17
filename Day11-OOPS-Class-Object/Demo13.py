
class Employee:

    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("The name and age of employee inside constructor is:", self.name,self.age)




#myobj1=Employee("Roshan") #TypeError: Employee.__init__() missing 1 required positional argument: 'local_age'
myobj1=Employee("Jack",18)
print("Name of the employee for myobj1:",myobj1.name)
print("Age of the employee for myobj1 :",myobj1.age)
myobj1.age=50
print("Age of the employee for myobj1 :",myobj1.age)
myobj2=Employee("Reena","45")
print("Name and age of the employee for myobj2:",myobj2.name,myobj2.age)
myobj3=Employee("John",56)
print("Name and age of the employee for myobj3:",myobj3.name,myobj3.age)

"""
Output : 
The name and age of employee inside constructor is: Jack 18
Name of the employee for myobj1: Jack
Age of the employee for myobj1 : 18
Age of the employee for myobj1 : 50
The name and age of employee inside constructor is: Reena 45
Name and age of the employee for myobj2: Reena 45
The name and age of employee inside constructor is: John 56
Name and age of the employee for myobj3: John 56
"""


