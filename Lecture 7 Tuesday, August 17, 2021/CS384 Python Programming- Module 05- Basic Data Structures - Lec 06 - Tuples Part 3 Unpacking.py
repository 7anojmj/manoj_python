
import os
os.system("cls")


def clear_the_terminal_screen():
    os.system("cls")


subjects_years = ('physics', 'chemistry', 1997, 2000)
print(subjects_years.index(1997))

numbers_tuple = (71, 12, 53, 44, 502)
characters_tuple = ("a", "b", "c", "d")

numbers_tuple = (1, 52, 13)
first, second, third = numbers_tuple
print(first, second, third)

numbers_tuple = (1, 52, 13, 450, 555, 19, 21, 1)
first, second, *others = numbers_tuple
print(first, second, *others)
print(first, second, others)

numbers_tuple = (1, 52, 13, 450, 555, 19, 21, 1)
first, second, *others, last = numbers_tuple
print(first, second, others, last)
