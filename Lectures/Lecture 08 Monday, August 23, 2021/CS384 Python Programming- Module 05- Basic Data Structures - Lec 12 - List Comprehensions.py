import math
import os
os.system('cls')
# os.system('clear')

List_of_squares = []

for x in range(5):
    print(x**2)
    List_of_squares.append(x**2)

print(List_of_squares)
# exit()
# os.system('cls')

List_of_squares = []
List_of_squares = [x**2 for x in range(5)]
print(List_of_squares)
# exit()

# Convert list items to absolute values
vec = [-4, -2, 0, 12, 14]
L = [abs(x) for x in vec]
print(L)
# Prints [4, 2, 0, 12, 14]


# Remove whitespaces of list items
colors = ['  red', '  gre en ', '                      blue     ']
print(colors)
L = [color.strip() for color in colors]
print(L)
# Prints ['red', 'green', 'blue']
exit()
