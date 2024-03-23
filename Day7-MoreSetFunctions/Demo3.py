#Create a set with add()

x={56,78,89}
print(x)
x.add(9)
print(x)

#x.update(89) #TypeError: 'int' object is not iterable
x.update([67,0,7.7,0])
print(x) #{0, 67, 7.7, 9, 78, 56, 89}

x.update(range(2),[3,4])
print(x) #{0, 1, 67, 3, 4, 7.7, 9, 78, 56, 89}


