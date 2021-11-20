
import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
#


#########
# Required Arguments
# Required arguments are the arguments passed to a function in correct positional order.
# Here, the number of arguments in the function call should match exactly with the function
# definition.
# To call the function printme(), you definitely need to pass one argument, otherwise it gives
# a syntax error as follows  # !/usr/bin/python3
# Function definition is here


def printme(str, age):
    "This prints a passed string into this function"
    print(str, age)
    return


# Now you can call printme function #Error
# printme("Hello World")
mystring = "Hi There"
age = 56
printme(mystring)


########
