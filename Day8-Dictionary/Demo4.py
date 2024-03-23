dict_name={1:'a',2:'b',3:'c'}
print(dict_name)
del dict_name[3]
print(dict_name) #{1: 'a', 2: 'b'}

dict_name.pop(1)
print(dict_name) #{2: 'b'}

#dict_name.pop(3) #KeyError: 3

#del dict_name[3] #KeyError: 3

dict_name={1:'a',2:'b',3:'c'}
print(dict_name.popitem()) #(3, 'c')
print(dict_name) #{1: 'a', 2: 'b'}

dict_name.clear()
print(dict_name) #{}