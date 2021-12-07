import os
os.system("cls")  # For Windows
# os.system("clear")  # For Linux & MAC

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)

var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)
    print("Good bye!")
# When the above code is executed, it produces the following result −
# 1 - Got a true expression value
# 100
# Good bye!

#####################
amount = int(input("Enter amount: "))
if amount < 1000:  # false
    discount = amount*0.05
    print("Discount", discount)
else:
    discount = amount*0.10
    print("Discount", discount)

print("Net payable:", amount-discount)


#####################
# Single Statement Suites
# If the suite of an if clause consists only of a single line, it may go on the same line as the
# header statement.
# Here is an example of a one-line if clause-
# #!/usr/bin/python3
var = 100
if (var == 100):
    print("Value of expression is 100")
print("Good bye!")


#####################
