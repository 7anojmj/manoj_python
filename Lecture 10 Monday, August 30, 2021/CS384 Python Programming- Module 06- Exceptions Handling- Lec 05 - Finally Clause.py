
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
    division = numerator/denominator
    print(division)
except (ZeroDivisionError, TypeError):
    print("There was some error in try clause: ZeroDivisionError or TypeError")
except:
    print("Unknown Error Occured")
finally:
    print("I will always execute whether  try succeeds or except succeeds!")

# exit()

# Try to open and write to a file that is not writable:

f = open("demofile.txt", "r")
try:
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file")
finally:
    print("Closing the file here")
    f.close()

print("Have A Good Day!")
