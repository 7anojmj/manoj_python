import os
os.system("cls")
# padding for float numbers
print("{:50.9f}".format(4412.2346789789654))

# integer numbers with minimum width filled with zeros
print("{:09d}".format(12))

# integer numbers with minimum width filled with zeros
print("{:5d}".format(12))

# padding for float numbers filled with zeros
print("{:08.3f}".format(12.2346))


# show the + sign
print("{:+f} {:+f}".format(12.23, -12.23))

# show the - sign only
print("{:-f} {:-f}".format(12.23, -12.23))

# show space for + sign
print("{: f} {: f}".format(12.23, -12.23))

# string padding with left alignment
print("{:5}".format("cat"))

# string padding with right alignment
print("{:>5}".format("cat"))

# string padding with center alignment
print("{:^5}".format("cat"))

# string padding with center alignment
# and '*' padding character
print("{:*^5}".format("cat"))
