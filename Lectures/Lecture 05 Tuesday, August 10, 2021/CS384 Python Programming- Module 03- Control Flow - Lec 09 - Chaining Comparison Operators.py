import os
os.system("cls")  # For Windows
# os.system("clear")  # For Linux & MAC

# x < y <= z is equivalent to x < y and y <= z,
x = 5
print("1 < x < 10")  # 1 < x and x < 10 --> 1 < 5 and 5 < 10 --> True and True
print(1 < x < 10)  # Evaluating the expression

print(10 < x < 20)
print(x < 10 < x*10 < 100)
print(x)
print(10 > x <= 9)
print(5 == x > 4)


# Python code to illustrate
# chaining comparison operators
a, b, c, d, e, f = 0, 5, 12, 0, 15, 15
exp1 = a <= b < c > d is not e is f

# (a <= b) and (b < c) and (c > d) and (d is not e) and (e is f)
#      true and true     and true  and      true     and true
print(exp1)
print(a is d)
exp2 = a is d > f is not c
exp3 = a >= b < c > d is not e is f
print(exp2)
print(exp3)
