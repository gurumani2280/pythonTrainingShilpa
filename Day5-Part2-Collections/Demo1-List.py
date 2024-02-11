#List Data Structure
l=[]
print(l)
print(type(l))

l.append(12)
print(l)

l1=[12,13,15,9,True]
print(l1)
print(l1[1])
print(l1[1:3])


#l2=list(12) #TypeError: 'int' object is not iterable
l2=list(range(0,10,2))
print(l2)

l3=list("Hello World")
print(l3)

for i in l2:
    print(i, end=" ")
print()
l4=list(l3)
print(l4)

l5=list([12,12.1,True,"Hello"])
print(l5)

del l5[1]
print(l5)
print(len(l5))

x="This is Pycharm"
l6=x.split()
print(l6)
print(type(l6))

l6[1]="Was"
print(l6)

