

import os
os.system("cls")
# os.system("clear")

# Types
numerator = 10
denominator = '0'  # 0, '0'
# division = numerator / denominator
# print(division)
# exit()
# ZeroDivisionError: division by zero
# TypeError: unsupported operand type(s) for /: 'int' and 'str'

try:
    division = numerator/denominator
    print(division)
except ZeroDivisionError:
    print("There was some error in try clause: ZeroDivisionError")
except TypeError:
    print("There was some error in try clause: TypeError")
except:
    print("Unknown Error Occured")


try:
    division = numerator/denominator
    print(division)
except (ZeroDivisionError, TypeError):
    print("There was some error in try clause: ZeroDivisionError or TypeError")
except:
    print("Unknown Error Occured")


print("Have A Good Day!")
