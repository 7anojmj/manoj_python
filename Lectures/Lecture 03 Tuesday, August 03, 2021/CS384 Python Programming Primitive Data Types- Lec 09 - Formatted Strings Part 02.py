# https: // www.programiz.com/python-programming/methods/string/format
# String format() Parameters
# format() method takes any number of parameters. But, is divided into two types of parameters:

# Positional parameters - list of parameters that can be accessed with index of parameter inside curly braces {index}
# Keyword parameters - list of parameters of type key = value, that can be accessed with key of parameter inside curly braces {key}
import os
os.system("cls")

# keyword arguments
# default arguments
print("Hello {}, your balance is {}.".format("Smile Please", 123.567))

# positional arguments
print("Hello {0}, your balance is {1}.".format("Smile Please", 123.567))

print("3rd print Hello {full_name}, your balance is {blc}.".format(
    name="Smile Please", blc=123.567, full_name="Sachin Tendulkar"))

print("Hello {name}, your balance is {blc}.".format(
    name="Smile Please", blc=123.567))


# keyword arguments
print("Hello {blc}, your balance is {name}.".format(
    name="Smile Please", blc=123.567))


# keyword arguments
print("6th print Hello {name}, your balance is {name}.".format(
    name="Smile Please", blc=123.567))

# Some errors

# mixed arguments
print("7th print Hello {0}, your balance is {blc}.".format(
    "Smile Please", blc=123.567))
