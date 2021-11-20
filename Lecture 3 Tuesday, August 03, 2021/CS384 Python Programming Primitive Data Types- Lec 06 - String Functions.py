# Till here done

import os
os.system("cls")
a = "Hello, World!    "
print(len(a))  # length of the string


# a = "                  Hello, World! "
# print(a)  # returns "Hello, World!"
# print(a.strip())  # returns "Hello, World!"

# a = "Hello, World!"
# print(a.lower())

# a = "hello world"
# # print(a.upper())
# # print(a.capitalize())

# a = "Hello, World!"
# print(a.replace("l", "z"))


a = "Hello, World!, India, Cat, !Umbrella, Toy"
print(a.split("!"))


countries = "India France UK America"
x = "France" in countries
print(x)


countries = "India France UK America"
x = "Bangladesh" not in countries
print(x)

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + ":" + b + "."
print(c)

age = 36
TXT = "My name is John, I am " + str(age) + " years old"
print(TXT)
