import os
os.system("cls")  # For Windows
# os.system("clear")  # For Linux & MAC

# Program to demonstrate conditional operator
a, b = 100, 200

# Copy value of a in min if a < b else copy b
min_element = a if a < b else b

print(min_element)
