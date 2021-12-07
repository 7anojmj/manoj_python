
import os
os.system("cls")
# os.system("clear")


def clear_the_terminal_screen():
    os.system("cls")


subjects_years = ['physics', 'chemistry', 1997, 2000]
numbers_list = [71, 12, 53, 44, 502, 666]
characters_list = ["a", "b", "c", "d"]

print(type("1.2"))

print(subjects_years)
print(numbers_list)
print(characters_list)

print('*'*30)
print("subjects_years[0]: ", subjects_years[0])
print("numbers_list[1:5]: ", numbers_list[1:5])

print(numbers_list)
print("Value available at index 2 : ", numbers_list[2])
numbers_list[2] = 2001
print("New value available at index 2 : ", numbers_list[2])
print(numbers_list)
numbers_list[2] = "Joker"
print("New value available at index 2 : ", numbers_list[2])
print(numbers_list)
print("Before deleting value at index 2 : ", numbers_list)
print(numbers_list)
del numbers_list[2]
print(numbers_list)
os.system("cls")
print("After deleting value at index 2 : ", numbers_list)
print("The length of the numbers_list is  : ", len(numbers_list))
print("The concatenation of the characters_list and numbers_list is  : ",
      characters_list + numbers_list)

# Traversing List
for x in numbers_list:
    print("The number read is ", x)

print("The last element in  numbers_list is  : ", numbers_list[-1])
print("The second last element in  numbers_list is  : ", numbers_list[-2])

print("The max element in  numbers_list is  : ", max(numbers_list))
print("The max element in  numbers_list is  : ", min(numbers_list))

subjects_years, numbers_list = [12, 'C++', 'Java', 'Python'], [456, 700, 200]
print("Max value element : ", max(subjects_years))
print("Max value element : ", max(numbers_list))
