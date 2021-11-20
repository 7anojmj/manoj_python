import os
os.system('cls')
# os.system('clear')


def clear_the_terminal_screen():
    os.system("cls")

# list = []
# tuple = ()
# dictionary = {}


car_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year_of_manufacture": 1952,
}
print(car_dictionary)
car_model = car_dictionary["model"]
car_year = car_dictionary["year"]
car_year_of_manufacture = car_dictionary["year_of_manufacture"]

print(car_model)
print(car_year)
print(car_year_of_manufacture)

# updating dictionary
print(f'Before changing {car_dictionary["year"]}')
car_dictionary["year"] = 2020
print(f'After changing {car_dictionary["year"]}')
# clear_the_terminal_screen()


# exit()
# Print Keys
for x in car_dictionary:
    print(x)
print('*'*30)
# Print Values
for x in car_dictionary:
    print(f'The key read is "{x}"')
    print(car_dictionary[x])  # car_dictionary[brand]

# Print Keys
for x in car_dictionary:
    print(x)

for x in car_dictionary.values():
    print(x)

# exit(0)
clear_the_terminal_screen()

# Loop through both keys and values, by using the items() method:
for x, y in car_dictionary.items():
    print(x, y)
exit()
