class myclass:
    pass
myobject=myclass() #object creation or class instantiation
print(myobject) #<__main__.myclass object at 0x00000238FDE75460>
print(type(myobject)) #<class '__main__.myclass'>

#myobject is a reference variable for object created at line 3.
#For one class we can create multiple object
#Using object reference,we can access class attributes or methods

myobject2=myclass()
