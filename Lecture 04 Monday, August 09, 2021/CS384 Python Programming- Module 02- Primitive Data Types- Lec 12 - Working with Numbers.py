# i++  # not allowed
# ++i are not allowed
a = 21
b = 10
c = 0
c = a + b  # 31
print("Line 1 - Value of c is ", c)
print(c)
c += a   # c = c + a 31 + 21
print("Line 2 - Value of c is ", c)
c *= a  # c = c *a
print("Line 3 - Value of c is ", c)
c /= a  # c = c /a
print("Line 4 - Value of c is ", c)
c = 2
c %= a  # c % a  84%21
print("Line 5 - Value of c is ", c)
c **= a  # c ** a ==> c ^ a
print("Line 6 - Value of c is ", c)
c = 23
a = 5
c //= a  # c = c // a
print("Line 7 - Value of c is ", c)
