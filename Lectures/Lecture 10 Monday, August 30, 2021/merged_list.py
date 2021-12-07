
import os
os.system("cls")


def clear_the_terminal_screen():
    os.system("cls")


subjects_years = ['physics', 'chemistry', 1997, 2000]
numbers_list = [1, 2, 3, 4, 5]
characters_list = ["a", "b", "c", "d"]

print(subjects_years)
print(numbers_list)
print(characters_list)

print('*'*30)

print("subjects_years[0]: ", subjects_years[0])
print("numbers_list[1:5]: ", numbers_list[1:5])

# exit()
print("Value available at index 2 : ", numbers_list[2])
numbers_list[2] = 2001
print("New value available at index 2 : ", numbers_list[2])

print("Before deleting value at index 2 : ", numbers_list)
print(numbers_list)
del numbers_list[2]
print("After deleting value at index 2 : ", numbers_list)

print("The length of the numbers_list is  : ", len(numbers_list))
print("The concatenation of the characters_list and numbers_list is  : ",
      characters_list + numbers_list)

# Traversing List
for x in numbers_list:
    print(x, end='#')

print("The last element in  numbers_list is  : ", numbers_list[-1])
print("The second last element in  numbers_list is  : ", numbers_list[-2])

print("The max element in  numbers_list is  : ", max(numbers_list))
print("The max element in  numbers_list is  : ", min(numbers_list))

subjects_years, numbers_list = ['C++', 'Java', 'Python'], [456, 700, 200]
print("Max value element : ", max(subjects_years))
print("Max value element : ", max(numbers_list))

numbers_list = [1, 52, 13, 450, 555, 19, 21, 1]

# list.append(obj)
# Appends object obj to list
numbers_list.append(99)
print(f'{numbers_list}')

# list.count(obj)
# # Returns count of how many times obj occurs in list
print(f'{numbers_list.count(1)}')

# exit()
# list.index(obj)
# # Returns the lowest index in list that obj appears
print(f'{numbers_list.index(1)}')

# list.insert(index, obj)
# # Inserts object obj into list at offset index
numbers_list.insert(0, -999)
print(f'{numbers_list}')

# list.pop(obj=list[-1])
# # Removes and returns last object or obj from list
print(f'{numbers_list}')
print(f'{numbers_list.pop()}')
print(f'{numbers_list}')

clear_the_terminal_screen()
# list.remove(obj)
# # Removes object obj from list
print("Remove")
print(f'{numbers_list}')
print(f'{numbers_list.remove(1)}')
print(f'{numbers_list}')

# list.sort([func])

print(f'{numbers_list}')
print(f'{numbers_list.sort()}')
print(f'{numbers_list}')

# list.reverse()
# Reverses objects of list in place
print(f'{numbers_list}')
print(f'{numbers_list.reverse()}')
print(f'{numbers_list}')

# list.extend(seq)
# # Appends the contents of seq to list
numbers_list.extend(characters_list)
print(f'{numbers_list}')

numbers_list = [1, 52, 13]
first, second, third = numbers_list
print(first, second, third)

numbers_list = [1, 52, 13, 450, 555, 19, 21, 1]
first, second, *others = numbers_list
print(first, second, *others)
print(first, second, others)

numbers_list = [1, 52, 13, 450, 555, 19, 21, 1]
first, second, *others, last = numbers_list
print(first, second, others, last)
