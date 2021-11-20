import math
import os
os.system('cls')
# os.system('clear')

# Python Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


def area_of_circle(radius):
    return math.pi * radius * radius


area = area_of_circle(5)


def area(radius): return math.pi * radius * radius


print(f"The area of the circle is '{area}'")
