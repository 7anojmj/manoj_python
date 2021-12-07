import math
import os
os.system('cls')
# os.system('clear')

# Python Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

def area_of_circle(radius):
    return math.pi * radius * radius

area = area_of_circle(1)

print(f"The area of the circle is '{area}'")

area_lambda_function = lambda radius : math.pi * radius * radius

print(f"The area of the circle is '{area_lambda_function(1)}'")

area_rectangle_function = lambda l,b : l*b

print(f"The area of the rectangle is '{area_rectangle_function(4,7)}'")
