import os
os.system("cls")  # For Windows
# os.system("clear")  # For Linux & MAC

for letter in 'Python':
    # traversal of a string sequence
    print('Current Letter :', letter)
print()  # Blank line


fruits = ['banana', 'apple', 'mango']
# traversal of List sequence
for x in fruits:
    print('Current fruit :', x)


print("Good bye!")


# Iterating by Sequence Index
# An alternative way of iterating through each item is by index offset into the sequence
# itself. Following is a simple example-
#!/usr/bin/python3
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print(index)
    print('Current fruit :', fruits[index])
print("Good bye!")
