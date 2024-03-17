"""Creating instance method
Instance method has self as first argument like constructor or init method.
"""
class Employee:
    company_name="ABC"
    weekly_work_hours=45
    def __init__(self,name,salary,age):
        self.name=name
        self.salary=salary
        self.age=age
    def printemployeedetail(self):
        print("Employee Name= {}, Employee salary={}, Employee age={}".format(self.name,self.salary,self.age) )


obj1=Employee("Shilpa",25000,12)
obj1.printemployeedetail()

"""
Output:
Employee Name= Shilpa, Employee salary=25000, Employee age=12
"""