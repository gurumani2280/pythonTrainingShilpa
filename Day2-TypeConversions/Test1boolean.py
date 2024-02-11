print(not True)
print(not(5==5))
print(not(5!=5))

a=True
print(type(a))
print(bool(5))
print(bool(0))
print(bool(-9))
print(bool(0.9))
print(bool(0.0))
print(bool("abc"))
print(bool(""))
print(bool('0'))
print(bool('0.0'))

#Any value other than zero is True
#-For int datatype, zero means false. All others true.
#-For float datatype, 0.0 is false. All others true.
#-For any string data type, empty string(single/double quotes without any character) will return false  otherwise true.