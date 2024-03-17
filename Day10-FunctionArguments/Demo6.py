#5We can give keyword variable length argument also using **
def user_check(**x):
    print(x)

user_check(name="Raj",age=9,email_id="abc.com")