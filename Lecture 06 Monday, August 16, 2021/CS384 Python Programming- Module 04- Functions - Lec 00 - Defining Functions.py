# Syntax
# def functionname(parameters):
#     "function_docstring"
#     function_suite
#     return [expression]

# Function definition is here
import os
os.system("cls")
# os.system("clear") #For mac/ubuntu


def printme_v2(p1, p2):
    print("The first parameter is : ", p1)
    print("The second parameter is : ", p2)
    printme("Again second call to the same function")

    return


def printme(toy):
    """This function prints anything on the screen that is passed to it """
    print(toy)
    return


print("CS384")

printme("This is first call to the user defined function!")
printme("Again second call to the same function")

printme_v2(10, "Joker")
printme_v2("Apple", [1, 2, 3])
