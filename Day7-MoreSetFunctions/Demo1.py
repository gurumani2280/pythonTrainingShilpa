#list of no:s which contains duplicate elements. Question is to remove the duplicates.
x=eval(input("Pls enter a list of numbers :"))
print(x)
list1=[]
for i in x:
    if i not in list1:
        list1.append(i)
print(list1)

#Another way of doing same thing using set() - set function
list2=list(set(x))
print(list2)


