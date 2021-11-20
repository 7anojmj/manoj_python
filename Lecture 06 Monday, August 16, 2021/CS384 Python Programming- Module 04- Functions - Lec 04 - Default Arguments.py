
import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
#

# Default Arguments
# A default argument is an argument that assumes a default value if a value is not provided
# in the function call for that argument. The following example gives an idea on default
# arguments, it prints default age if it is not passed.
#!/usr/bin/python3

# Function definition is here


def printinfo(name="Opera", age=25):  # always at last
    "This prints a passed info into this function"
    print("Name: ", name)

    print("Age ", age)
    return


# Now you can call printinfo function

printinfo("Joker", 45)
printinfo("Alien")
printinfo()

printinfo(age=50, name="miki")
printinfo(age=50)
printinfo(name="miki")
