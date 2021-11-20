
import os
os.system("cls")


def clear_the_terminal_screen():
    os.system("cls")


subjects_years = ['physics', 'chemistry', 1997, 2000]
numbers_list = [1, 2, 3, 4, 5]
characters_list = ["a", "b", "c", "d"]


numbers_list = [1, 52, 13]
first, second, third = numbers_list
print(first, second, third)

numbers_list = [1, 52, 13, 450, 555, 19, 21, 1]
first, second, *others = numbers_list
print(first, second, *others)
print(first, second, type(others))

numbers_list = [1, 52, 13, 450, 555, 19, 21, 15]
first, second, *others, slast, last = numbers_list
print(first, second, others, slast, last)
