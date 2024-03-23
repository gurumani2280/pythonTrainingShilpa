dict1={"Emp_ID":1,"Emp_Name":"Navin","Dept":"CS","Sal":25000}
print(dict1["Emp_ID"]) #1

#print(dict1[1]) #KeyError: 1

if 1 in dict1:
    print(dict1[1])

else:
    print("1 is not present in the dictionary")

print(dict1.get("Emp_Name")) #Navin
print(dict1.get("Emp_NAme")) #None

print(dict1.get("Emp_NAme","Default")) #Default
print(dict1.get("Dept","Default")) #CS