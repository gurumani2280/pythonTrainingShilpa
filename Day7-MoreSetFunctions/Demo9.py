#Write a program to print vowels present in a string

x=input("Pls enter a string :")
print(x)
vowels=['a','e','i','o','u']
#v=set()
#for i in x:
    #if i in vowels:
        #v.add(i)

#print(v)

#Another way of doing same thing
set1=set(x)
set2=set(vowels)
set3=set1.intersection(set2)
print(set3)

