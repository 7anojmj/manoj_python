
import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
#
total = 0  # This is global variable.
# Function definition is here


def sum(arg1, arg2):
    # global total
    # Add both the parameters and return them."
    total = arg1 + arg2  # Here total is local variable.
    print("Inside the function local total : ", total)
    return total


# Now you can call sum function
print("Before fun call : ", total)
total = sum(10, 20)
print("Outside the function global total : ", total)
