
import os
os.system("cls")
# os.system("clear")


def clear_the_terminal_screen():
    os.system("cls")


subjects_years = ('physics', 'chemistry', 1997, 2000)
numbers_tuple = (71, 12, 53, 44, 502)
characters_tuple = ("a", "b", "c", "d")

print(subjects_years)
print(numbers_tuple)
print(characters_tuple)


print('*'*30)
os.system("cls")
print(type(subjects_years))
print("subjects_years[0]: ", subjects_years[0])
print("numbers_tuple[1:5]: ", numbers_tuple[1:5])
os.system("cls")
# clear_the_terminal_screen()
# print(numbers_tuple)
# print("Value available at index 2 : ", numbers_tuple[2])
# # numbers_tuple[2] = 2001
# print("New value available at index 2 : ", numbers_tuple[2])
# print(numbers_tuple)
# numbers_tuple[2] = "Joker"
# print("New value available at index 2 : ", numbers_tuple[2])
# print(numbers_tuple)
# exit()
# print("Before deleting value at index 2 : ", numbers_tuple)
# print(numbers_tuple)
# del numbers_tuple[2]

os.system("cls")
print("After deleting value at index 2 : ", numbers_tuple)
print("The length of the numbers_tuple is  : ", len(numbers_tuple))
print("The concatenation of the characters_tuple and numbers_tuple is  : ",
      characters_tuple + numbers_tuple)

mylist = [1, 2]
mytuple = (1, 2)


# Traversing List
for x in numbers_tuple:
    print("The number read is ", x)

print("The last element in  numbers_tuple is  : ", numbers_tuple[-1])
print("The second last element in  numbers_tuple is  : ", numbers_tuple[-2])

print("The max element in  numbers_tuple is  : ", max(numbers_tuple))
print("The max element in  numbers_tuple is  : ", min(numbers_tuple))

subjects_years, numbers_tuple = ('C++', 'Java', 'Python'), (456, 700, 200)
print("Max value element : ", max(subjects_years))
print("Max value element : ", min(numbers_tuple))
