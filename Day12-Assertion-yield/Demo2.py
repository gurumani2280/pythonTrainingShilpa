x=5
y=5
print(x==y)
assert x==y, f"x {x} and y {y} values are not matching"
print("assertion passed")


"""
True
assertion passed
"""

"""
Assert Syntax:
asset <conditional exp>,"error message"
Conditional expression will be evaluated and if its true then program will continue.
If conditional evaluation is false, then program will terminate by raising assertion error and error message will also be printed.
Looking into this error, programmer can fix the code.
Error message part is optional.
"""