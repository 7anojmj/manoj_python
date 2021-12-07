import time


import os
os.system("cls")


def divison(numbers):
    for n in numbers:
        time.sleep(1)
        print("\nDouble:", n/5)


def multiplication(numbers):
    for n in numbers:
        time.sleep(1)
        print("\nSquare:", n*5)


numbers = [10, 20, 30, 40, 50]
begintime = time.time()
divison(numbers)
multiplication(numbers)
endtime = time.time()
print("The total time taken:", endtime-begintime)
