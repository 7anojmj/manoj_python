import math
import os
os.system('cls')


def x(a): return a + 10


print(x(5))

# os.system('clear')

# Python Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


def area_of_circle(radius):
    return math.pi * radius * radius


area = area_of_circle(1)

print(f"The area of the circle is '{area}'")


def area_lambda_function(radius): return math.pi * radius * radius
#area = lambda radius : math.pi * radius * radius


print(f"The area of the circle is '{area_lambda_function}'")
