import os
os.system("cls")
# integer arguments
print("The number is:{:d}".format(123))

# float arguments
print("The float number is:{:f}".format(123.45))

# octal, binary and hexadecimal format
print("bin: {0:b}, oct: {0:o}, hex: {0:x}".format(12))


# integer numbers with minimum width
print("{:d}".format(12))
print("{:15d}".format(12))
# width doesn't work for numbers longer than padding
print("{:d}".format(1234))
print("{:2d}".format(1234))
print("Phone Number: {:30d}".format(9876543210))
print("Aadhar Number: {:30d}".format(1234987612349876))
print("Credit Card Number: {:30d}".format(7777987612349876))
