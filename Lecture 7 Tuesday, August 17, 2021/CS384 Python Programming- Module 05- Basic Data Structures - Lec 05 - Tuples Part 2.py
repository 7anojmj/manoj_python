
import os
os.system("cls")


def clear_the_terminal_screen():
    os.system("cls")


subjects_years = ('physics', 'chemistry', 1997, 2000)
numbers_tuple = (71, 12, 53, 44, 502)
characters_tuple = ("a", "b", "c", "d")

print(subjects_years)
print(numbers_tuple)
print(characters_tuple)

print('*'*30)

# list.append(obj)
# Appends object obj to list
# print(f'{numbers_tuple}')
# numbers_tuple.append(99)
# numbers_tuple.append(111)
# print(f'{numbers_tuple}')
# list.count(obj)
# # Returns count of how many times obj occurs in list
print(f'{numbers_tuple.count(71)}')

# list.index(obj)
# # Returns the lowest index in list that obj appears
os.system("cls")
print(f'{numbers_tuple}')
print(f'{numbers_tuple.index(71)}')
# list.insert(index, obj)
# Inserts object obj into list at offset index
# numbers_tuple.insert(5, -999)
print(f'{numbers_tuple}')

# list.pop(obj=list[-1])
# # Removes and returns last object or obj from list
# os.system("cls")
# print(f'{numbers_tuple}')
# print(f'{numbers_tuple.pop()}')
# print(f'{numbers_tuple}')

clear_the_terminal_screen()
# list.remove(obj)
# # Removes object obj from list
# print("Remove")
# print(f'{numbers_tuple}')
# print(f'{numbers_tuple.remove(555)}')
# print(f'{numbers_tuple}')

# list.sort([func])
clear_the_terminal_screen()
print(f'{numbers_tuple}')
newtuple = sorted(numbers_tuple)
print(f'{newtuple}')

# list.reverse()
# Reverses objects of list in place
# print(f'{numbers_tuple}')
# print(f'{numbers_tuple.reverse()}')
# print(f'{numbers_tuple}')

# list.extend(seq)
# # Appends the contents of seq to list
numbers_tuple.extend(characters_tuple)
# print(f'{numbers_tuple}')

exit()
