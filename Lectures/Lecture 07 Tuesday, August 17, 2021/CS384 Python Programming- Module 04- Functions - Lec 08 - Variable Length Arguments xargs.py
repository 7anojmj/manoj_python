
import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
#

mylist = [1, 2, 3]
print(mylist, type(mylist))

mylist = (1, 2, 3)
print(mylist, type(mylist))


def summation(*numbers):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(numbers)
    print(type(numbers))
    for x in numbers:
        print("The read number is :", x)


# Now you can call summation function
summation(70, 60, 50, 3, 6, "CS384")


# Variable-length Arguments
# You may need to process a function for more arguments than you specified while defining
# the function. These arguments are called variable-length arguments and are not named in
# the function definition, unlike required and default arguments.
# Syntax for a function with non-keyword variable arguments is given belowdef functionname([formal_args, ] * var_args_tuple):
# "function_docstring"
# function_suite
# return [expression]

# An asterisk(*) is placed before the variable name that holds the values of all nonkeyword
# variable arguments. This tuple remains empty if no additional arguments are specified
# during the function call. Following is a simple example  # !/usr/bin/python3

# # Function definition is here


# When the above code is executed, it produces the following result
# Output is :
# 10
# Output is :
# 70
# 60
# 50
