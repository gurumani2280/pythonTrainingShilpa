#Class is a blue print to create an object.
"""
Whatever variable created inside a class directly is a static/class variable.
Static/Class variable is common to all the objects.
if you create any variable using reference variable, then it is called as instance variable.
Instance variable value could be specific for each object
__init__() - This is a special method also known as Constructor
init method will be executed automatically when ever we create object of that class
"""
class Person:
    country="India" #Static variable or class variable


    def __init__(self,name,age,dept):
        print("Creating Object")
        self.name=name
        self.age=age
        self.dept=dept

