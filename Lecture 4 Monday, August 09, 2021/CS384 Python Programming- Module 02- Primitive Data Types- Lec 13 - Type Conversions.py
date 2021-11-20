

# Python code to demonstrate Type conversion
# using  ord(), hex(), oct()
import os
os.system("cls")
# initializing integer
s = '7'

# printing character converting to integer
c = ord(s)
print("After converting character to integer : ", end="")
print(c)

# printing integer converting to hexadecimal string
c = hex(56)
print("After converting 56 to hexadecimal string : ", end="")
print(c)

# printing integer converting to octal string
c = oct(56)
print("After converting 56 to octal string : ", end="")
print(c)

# Convert ASCII value to characters
a = chr(97)
b = chr(65)

print(a)
print(b)


print("int(-45.2) : ", int(-45.2))
print("float(-45) : ", float(-45))
print("complex(-45,9) : ", complex(-45, 9))
print("abs(-45) : ", abs(-45))
print("abs(100.12) : ", abs(100.12))
