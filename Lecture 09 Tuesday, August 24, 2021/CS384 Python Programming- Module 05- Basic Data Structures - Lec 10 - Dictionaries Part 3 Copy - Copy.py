import os
os.system('cls')
# os.system('clear')

# Copy a Dictionary
car_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car_dictionary)
copy_of_dictionary = car_dictionary
print(copy_of_dictionary)

print("now deleting model")
del car_dictionary['model']
print(car_dictionary)
print(copy_of_dictionary)

os.system('cls')

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# Example
# Make a copy of a dictionary with the copy() method:

car_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
copy_of_dictionary = car_dictionary.copy()
print(copy_of_dictionary)
os.system('cls')

del car_dictionary['model']
print(car_dictionary)
print(copy_of_dictionary)
# Example
# Make a copy of a dictionary with the dict() function:

car_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
copy_of_dictionary = dict(car_dictionary)
print(copy_of_dictionary)

# More than one entry per key not allowed.
# Which means no duplicate key is allowed.
# When duplicate keys encountered during assignment,
# the last assignment wins. For example −

os.system('cls')

car_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "brand": "Maruti",
    "brand": "Audi",
}

print(car_dictionary)
