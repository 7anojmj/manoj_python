

import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
#


def Fibonacci(n):

    if n < 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 0:
        return 0
    # Second Fibonacci number is 1
    elif n == 1:
        return 1
    # Third Fibonacci number is recursive function
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


print("Fibonacci(0) = ", Fibonacci(0))
print("Fibonacci(1) = ", Fibonacci(1))

n = 60
for i in range(n):
    if i >= 2:
        print("Fibonacci {} = Fibonacci {} + Fibonacci {}".format(i, i-1, i-2))
        print("Fibonacci(", i, ") = ", Fibonacci(i))
