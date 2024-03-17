"""There are 4 types of actual arguments.
1.Positional Arguments or Required Arguments
2.Keyword Arguments or Named Arguments
3.Default Arguments
4.Variable length Arguments
"""

def average(*z):
    print("Average of no:s-input", z)
    if len(z)==0:
        return 0
    else:
        return sum(z) / len(z)

print(average(100))
print(average())
print(average(10,20,30,40,50,60))