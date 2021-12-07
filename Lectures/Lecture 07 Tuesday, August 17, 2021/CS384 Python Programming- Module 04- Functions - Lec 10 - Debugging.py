
import os
os.system("cls")
# os.system("clear") #For mac/ubuntu
#


def summation(*numbers):
    total = 0
    for x in numbers:
        print("The number read now is : ", x)
        total += x
    return total


lucky_number = 99
total_sum = summation(10, 20, 30)
print("Hello WOrld")
print(total_sum)
