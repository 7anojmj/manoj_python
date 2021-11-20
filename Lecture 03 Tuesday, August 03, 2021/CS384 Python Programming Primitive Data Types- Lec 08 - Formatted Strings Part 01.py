# https: // www.programiz.com/python-programming/methods/string/format
# String format() Parameters
# format() method takes any number of parameters. But, is divided into two types of parameters:

# Positional parameters - list of parameters that can be accessed with index of parameter inside curly braces {index}
# Keyword parameters - list of parameters of type key = value, that can be accessed with key of parameter inside curly braces {key}

import os
os.system("cls")

# default arguments
# print("Hello {}, \n Your balance is {}.".format("Smile Please", 123.567))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Smile Please", 123.567))
# positional arguments
print("Hello {1}, your balance is {0}.".format("Smile Please", 123.567))


# positional arguments
print("Hello {0}, your balance is {0}.".format("Smile Please", 123.567))

# positional arguments
print("Hello {1}, your balance is {1}.".format("Smile Please", 123.567))

# positional arguments
print("Hello {2}, your balance is {1}.".format(
    "Smile Please", 123.567, "Ramesh"))

# ERROR arguments
print("Hello {}, your balance is {}.".format("Smile Please", 12))

os.system("cls")
name = 'Tushar'
age = 23
subject = "CS384"
print(
    f"Hello, My name is {name} and I'm {age} years old. I am learning {subject}")

exit()
