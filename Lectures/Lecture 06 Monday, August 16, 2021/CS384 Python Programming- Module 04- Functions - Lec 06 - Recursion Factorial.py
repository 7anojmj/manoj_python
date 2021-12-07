
import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
#


def factorial(num):
    """This is a recursive function
    to find the factorial of an integer"""

    if num == 1 or num == 0:
        return 1
    else:
        return (num * factorial(num-1))
        # 3 * 2 *  1
        ##


num = 3
print("The factorial of", num, "is", factorial(num))
