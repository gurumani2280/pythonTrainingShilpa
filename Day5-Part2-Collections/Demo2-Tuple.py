t=()
print(type(t))

t1=(78) #While giving single element inside tuple, be careful cos it considers as int/float/bool/string
print(t1)
print(type(t1))  #<class 'int'>

t2=(78,)
print(t2)
print(type(t2))

t3=(67,8.8,"hello")
print(t3)
#del t3[2] #TypeError: 'tuple' object doesn't support item deletion

#t3[0]=90 #TypeError: 'tuple' object does not support item assignment

#Tuple is read-only version of list

t4=tuple("hello")
print(t4)

l5=list(t3)
print(l5)

#Practice all the things done in list for tuple.
#Create notes2 for tuple as like list.