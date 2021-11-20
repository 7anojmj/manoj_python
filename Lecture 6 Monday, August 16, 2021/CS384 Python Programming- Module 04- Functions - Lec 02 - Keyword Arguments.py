

import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
#
#
# # Keyword Arguments
# Keyword arguments are related to the function calls. When you use keyword arguments
# in a function call, the caller identifies the arguments by the parameter name.
# This allows you to skip arguments or place them out of order because the Python
# interpreter is able to use the keywords provided to match the values with parameters. You
# # !/usr/bin/python3
# can also make keyword calls to the printme() function in the following ways

# Function definition is here


def printinfo(name, myage, gender):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", myage)
    print("Gender ", gender)
    return


# Now you can call printinfo function
printinfo("Joker", 42, "M")
# printinfo(name="Joker", age=42)
printinfo(myage=50, gender='M', name="miki")
