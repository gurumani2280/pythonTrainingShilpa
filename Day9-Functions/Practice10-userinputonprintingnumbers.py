#Write a function to ask user input no: till user wants and at the end count of positive no:s, negative no:s and zeros entered by the user.
def userinput_count():
    negative_list=[]
    positive_list = []
    Zero_list=[]
    while True:
        x=input("Do you want to enter a number? Y/N")
        if x.lower().strip()=='y':

            i=int(input("Enter a number: (Positive/Negative)"))
            if i==0:
                Zero_list.append(i)
            elif i>0:
                positive_list.append(i)
            elif i<0:
                negative_list.append(i)
        else:
            break
    print("Zero List=", Zero_list)
    print("Positive List=", positive_list)
    print("Negative List=", negative_list)

userinput_count()