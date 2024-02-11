a=9
print(id(a))
print(id(9))

b=8
print(id(b))

c=8
print(id(c))

a=a+1
print(a)
print(id(a))

s="high"
print(id(s))
x="high"
print(id(x))
print(s is x)
print(s is not x)

s=s+"hello"
print(s)
print(id(s))
print(s is x)

print(id("high"))
print(s)
print(id(s))

print(id(9))

#Id represents the kind of address stored in the variable
#"is" is a identity operator and will return True/False if they have same address, otherwise false
#"is not" is a identity operator and will return true/false if they have different address.



