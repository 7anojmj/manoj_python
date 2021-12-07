import os
os.system("cls")  # For Windows
# os.system("clear")  # For Linux & MAC


a = 21
b = 21
c = 0

if (a == b):
    print("Line 1 - a is equal to b")

else:
    print("Line 1 - a is not equal to b")
    print("Hello World")
    print("Hello My World")

    print("End of Program")


if (a != b):
    print("Line 2 - a is not equal to b")
else:
    print("Line 2 - a is equal to b")


if (a < b):
    print("Line 4 - a is less than b")
else:
    print("Line 4 - a is not less than b")

if (a > b):
    print("Line 5 - a is greater than b")
else:
    print("Line 5 - a is not greater than b")

a = 5
b = 20
if (a <= b):
    print("Line 6 - a is either less than or equal to  b")
else:
    print("Line 6 - a is neither less than nor equal to  b")

if (b >= a):
    print("Line 7 - b is either greater than  or equal to b")
else:
    print("Line 7 - b is neither greater than  nor equal to b")
