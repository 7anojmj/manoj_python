
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


numbers_list = [1, 52, 13, 450, 555, 19, 21, 1]

# list.append(obj)
# Appends object obj to list
print(f'{numbers_list}')
numbers_list.append(99)
numbers_list.append(111)
print(f'{numbers_list}')
# exit()
os.system("cls")
# list.count(obj)
# # Returns count of how many times obj occurs in list
print(f'{numbers_list.count(1)}')
print(f'{numbers_list.count(52)}')

# exit()
# list.index(obj)
# # Returns the lowest index in list that obj appears
# os.system("cls")
print(f'{numbers_list}')
print(f'{numbers_list.index(99)}')
print(f'{numbers_list.index(1)}')

# list.insert(index, obj)
# # Inserts object obj into list at offset index
numbers_list.insert(5, -999)
print(f'{numbers_list}')

# list.pop(obj=list[-1])
# # Removes and returns last object or obj from list
os.system("cls")
print(f'{numbers_list}')
print(f'{numbers_list.pop()}')
print(f'{numbers_list}')

print(f'{numbers_list.pop()}')
# exit()
clear_the_terminal_screen()
# list.remove(obj)
# # Removes object obj from list
print("Remove")
print(f'{numbers_list}')
print(f'{numbers_list.remove(555)}')
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

exit()
