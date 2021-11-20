
import os
os.system("cls")
a = 60
# 60 = 0011 1100
b = 13
# 13 = 0000 1101
print('a=', a, ':', bin(a), 'b=', b, ':', bin(b))
###################
c = 0
c = a & b
# 12 = 0000 1100
print("result of AND is ", c, ':', bin(c))
###################


a = 60
# 60 = 0011 1100
b = 13
# 13 = 0000 1101

c = a | b
# 61 = 0011 1101
print("result of OR is ", c, ':', bin(c))

a = 60
# 60 = 0011 1100
b = 13
# 13 = 0000 1101

c = a ^ b
# 49 = 0011 0001
print("result of EXOR is ", c, ':', bin(c))

a = 60
# 60 = 0011 1100
b = 13
# 13 = 0000 1101
c = a << 1
print("result of LEFT SHIFT is ", c, ':', bin(c))

a = 60
# 60 = 0011 1100
b = 13
# 13 = 0000 1101
c = a >> 1
# 15 = 0000 1111

print("result of RIGHT SHIFT is ", c, ':', bin(c))
