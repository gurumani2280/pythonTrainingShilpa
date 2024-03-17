"""Creating class method
class method will have cls as first argument and @classmethod
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

    @classmethod
    def display_work_hours(cls):
        print("{} has working hours {}".format(cls.company_name,cls.weekly_work_hours))

Employee.display_work_hours()
obj1=Employee("Shilpa",25000,12)
obj1.display_work_hours()
obj1.printemployeedetail()


"""
Output:
ABC has working hours 45
ABC has working hours 45
Employee Name= Shilpa, Employee salary=25000, Employee age=12
"""