a='test'
#b=int(a) #ValueError: invalid literal for int() with base 10: 'test'

d='10'
c=int(d)
print(c) #10

#d='1abc'
#c=int(d) #ValueError: invalid literal for int() with base 10: 'abc' #invalid literal for int() with base 10: '1abc'
#print(c)

x=7.9
y=int(x)
print(y)

p=True
q=int(p)
print(q)

p=False
q=int(p)
print(q)



#For String to int conv,if string content is having only integer(even decimal wont be considered) it will return the int value otherwise error
#For Float to int conv, it will return non decimal part and ignore the decimal part
#For bool to int conv,it will 1 for true and 0 for False.