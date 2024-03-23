def user_check1(*x,**y):
    print(x,y)

user_check1(4,5) #(4, 5) {}
user_check1(name="John") #() {'name': 'John'}
user_check1(30,40,name="Raj",id=3) #(30, 40) {'name': 'Raj', 'id': 3}