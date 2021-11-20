import os
os.system('cls')
# os.system('clear')


# Check if "model" is present in the dictionary:

car_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "cs384" in car_dictionary:
    print("Yes, 'model' is one of the keys in the car_dictionary dictionary")
else:
    print("No such key is present ")
# Print the number of items in the dictionary:

os.system('cls')

print(len(car_dictionary))
# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

car_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(car_dictionary)
car_dictionary["color"] = "red"
car_dictionary["airbag"] = "yes"
print(car_dictionary)
# os.system('cls')

# Removing Items
# The pop() method removes the item with the specified key name:

print(car_dictionary)
car_dictionary.pop("model")
print(car_dictionary)
# The del keyword removes the item with the specified key name:
del car_dictionary["color"]
print(car_dictionary)


os.system('cls')

# The del keyword can also delete the dictionary completely:
car_dictionary.clear()
print(car_dictionary)
car_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del car_dictionary
# this will cause an error because "car_dictionary" no longer exists.
print(car_dictionary)
