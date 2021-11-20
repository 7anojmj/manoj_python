import csv
import os
import openpyxl
os.system('cls')
# os.system('clear')
# https://www.tutorialspoint.com/python/os_file_methods.htm

# print(dir(os))
# print(dir(openpyxl))

print(os.name)
print("Current Working Dir=", os.getcwd())  # Current working directory


os.chdir(r"c:\Windows")
print("Current Working Dir=", os.getcwd())  # Current working directory
os.getcwd()


os.chdir(r"d:\\")
print("Current GET CWD")
print(os.getcwd())


print(os.environ)

print(print(os.environ["TMP"]))
print(print(os.environ["ALLUSERSPROFILE"]))

exit()
