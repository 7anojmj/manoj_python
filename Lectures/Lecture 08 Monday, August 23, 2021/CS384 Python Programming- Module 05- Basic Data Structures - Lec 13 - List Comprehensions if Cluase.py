import math
import os
os.system('cls')
# os.system('clear')

# This list comprehension is the same as a for loop that contains an if statement:

vec = [-4, -2, 0, 2, 4]
L = []
for x in vec:
    if x >= 0:
        L.append(x)
# print(L)
# Prints [0, 2, 4]
# Filter list to exclude negative numbers


# Convert list items to absolute values
vec = [-4, -2, 0, 12, 14]
L = [abs(x) for x in vec]
print(L)

vec = [-4, -2, 0, 2, 4]

L = [x for x in vec if x < 0]
print(L)

vec = [-4, -2, 0, 2, 4]
L = []
for x in vec:
    if x < 0:
        L.append(x)
print(L)
# Prints [0, 2, 4]
