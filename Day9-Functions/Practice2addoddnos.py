#To print sum of all odd no:s from 1 to n.(You can "n" from the user)

def add_odd(n):
    print("Input is:",n)
    x_sum = 0
    for i in range(1,n):

        if (i%2!=0):
            print(i)
            x_sum = x_sum+i
            i = i+1
    print("The Final output is :",x_sum)

add_odd(int(input("Enter a number to add all the odd no:s - ")))

