# https://www.programiz.com/python-programming/set
# A set is an unordered collection of items. Every set element
# is unique (no duplicates) and must be immutable (cannot be changed).
import os
os.system("cls")
# os.system("clear")

my_set = {1, 3, 4, 5, 6, 1, 2, 3, 3, 7}
print(my_set)
print(type(my_set))
# exit()
# set of mixed datatypes
my_set = {1.0, "Hello", (1, 2, 3)}
#my_set = {1.0, "Hello", [1, 2, 3]}
print(my_set)
# exit(0)
# We cannot access or change an element of a set using indexing or slicing.
# Set data type does not support it.

# my_set[0]

# add an element
my_set.add(99)
print(my_set)

my_set.update([66, 77, 88])
print(my_set)
# exit()
# discard an element
my_set.discard(77)
print(my_set)
# exit()
# Set union method

os.system("cls")
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)  # Or / Union
print(A & B)  # And / Intersection
print(A - B)  # Difference

# Symmetric Difference of A and B is a set of elements in A and B
# but not in both (excluding the intersection).

print(A ^ B)  # Symmetric Difference

list222 = [1, 2, 3, 3, 3, 3, 4, 2, 2, 1, 4, 4, 1, 1]
temp = set(list222)
print(temp)
