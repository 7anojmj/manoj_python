
import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
# ############
# Name does not change anything. indexing does
# There is one more example where argument is being passed by reference and the
# reference is being overwritten inside the called function.
# Pass by Reference vs Value
# All parameters (arguments) in the Python language are passed by reference. It means if
# you change what a parameter refers to within a function, the change also reflects back in
# the calling function.
# For example
#!/usr/bin/python3

# Function definition is here


def changeme_by_reference(joker):  # joker = [10, 20 , 30 ]
    #mylist = [10, 20, 30]
    "This changes a passed list into this function"
    print("Values inside the function before change: ", joker)
    joker[2] = 50  # Indexing
    print("Values inside the function after change: ", joker)
    return


def changeme_by_value(mylist):  # [10, 20, 30]
    "This changes a passed list into this function"
    print("Values inside the function before change: ", mylist)
    mylist = [1, 2, 3, 4]
    print("Values inside the function after change: ", mylist)
    return


mylist = [10, 20, 30]
print("Values before calling function: ", mylist)
changeme_by_reference(mylist)
print("Values outside the function: ", mylist)
# changeme_by_value(mylist)
# print("Values outside the function: ", mylist)
# # Now you can call changeme_by_reference function
# mylist = [10, 20, 30]
