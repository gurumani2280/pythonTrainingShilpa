#Take age as user input and return if person is eligible to vote or not

def age_eligibility_check(n):
    if n>=18:
        print("The person is eligible to vote")
    else:
        print("The person is not eligible to vote")

n=int(input("Enter the age:"))
age_eligibility_check(n)
print()


print("Alternate Method:")
def age_eligibility_check(n):
    if n>=18:
        return "eligible"
    else:
        return "not-eligible"

n=int(input("Enter the age:"))
print(age_eligibility_check(n))
