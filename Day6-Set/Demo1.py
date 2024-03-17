s1={67}
print(type(s1))
print(s1)

s2=set()
print(s2)
print(type(s2))

#print(s1[0]) TypeError: 'set' object is not subscriptable

s1.add(89)
print(s1)
s1.update((67,90,89,"Hi",9.9))
print(s1)

s1.add(3)
print(s1)

#for i in s1:
    #print(i, end=" ")
#print()
print(s1.pop())
print(s1)

#s2=frozenset(s1) #'frozenset' object has no attribute 'add'
s2.add(90)
print(s2)



#Create a set and take user input for no.of cmds, and perform the cmds as per the user input.

