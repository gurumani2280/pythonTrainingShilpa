#Questions:
#Take one user input string and find the frequency of each character inside the input string.
#Input : Hello
#Output : h=1,e=1,l=2,o=1

x=input("Enter a string:")
#print(x)
#for i in set(x):
    #print(i,x.count(i))

#Another way of doing the same pgm:
#dict1={}
#for i in x:
    #dict1[i]=dict1.get(i,0)+1
    #print(i,dict1)
#print("Final Dict:",dict1)

#Another way of doing the same pgm:
dict2={}
for i in set(x):
    dict2[i]=x.count(i)
print("Final Dict:", dict2)



