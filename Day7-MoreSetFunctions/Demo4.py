x=set({45,67,89,100,100})
print(x) #{89, 67, 100, 45}


y=x.copy()
print(y)

print(x.pop()) #89
print(x) #{67, 100, 45}

x.remove(67)
print(x) #{100, 45}

#x.remove(200) #KeyError: 200

x.discard(100)
print(x) #{45}

x.discard(200) #No error on discard()

#Difference b/n Remove() and Discard() in set.
#Remove(element) - Removes the element if present inside set and if element is not present, throws error
#Discard(element)- discards the element if present inside set and if element is not present, no error is returned
#pop()- removes the random element if set has elements and if set is empty, it will throw Keyerror

print(y) #{89, 67, 100, 45}
y.clear()
print(y) #set()

#y.pop() #KeyError: 'pop from an empty set'

print(x)
#x.pop(45) #TypeError: set.pop() takes no arguments (1 given)



