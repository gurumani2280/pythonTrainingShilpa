def inf_sequence():
    num = 0
    while num<=10:
        yield num
        num += 1

def sequence(x):
    num = 0
    while num<=x:
        yield num
        num += 1

for i in inf_sequence():
    print(i, end=" ")
print()
for i in sequence(100):
    print(i, end=" ")
