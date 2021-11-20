# https://docs.python.org/3/library/exceptions.html

import os
os.system("cls")
# os.system("clear")

# Types
numerator = 10
denominator = '0'  # 0, '0'
# division = numerator / denominator
# print(division)

# ZeroDivisionError: division by zero
# TypeError: unsupported operand type(s) for /: 'int' and 'str'

try:
    division = numerator/denominator  # error line
    print(division)
except ZeroDivisionError:
    print("ZeroDivisionError : There was some error in try clause:")
except:
    print("There was some other exception then ZeroDivisionError")

print("Have A Good Day!")
