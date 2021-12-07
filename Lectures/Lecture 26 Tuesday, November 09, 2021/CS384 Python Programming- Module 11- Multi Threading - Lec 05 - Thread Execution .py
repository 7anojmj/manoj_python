# from threading import *
import time
import threading

import os
os.system("cls")


def divison(numbers):
    for n in numbers:
        time.sleep(1)
        print("\n Diving by 5:", n/5)


def multiplication(numbers):
    for n in numbers:
        time.sleep(1)
        print("\nMultiplying by 5:", n*5)


def subtraction(numbers):
    for n in numbers:
        time.sleep(1)
        print("\nSubtraction by 5:", n-5)


def addition(numbers):
    for n in numbers:
        time.sleep(1)
        print("\nAddition by 5:", n+5)

numbers = [10, 20, 30, 40, 50]


begintime = time.time()
divison(numbers)
multiplication(numbers)
addition(numbers)
subtraction(numbers)

t1 = threading.Thread(target=divison, args=(numbers,))
t2 = threading.Thread(target=multiplication, args=(numbers,))
t3 = threading.Thread(target=addition, args=(numbers,))
t4 = threading.Thread(target=subtraction, args=(numbers,))


t1.start()
t2.start()
t3.start()
t4.start()


t1.join()
t2.join()

t3.join()
t4.join()
endtime = time.time()
print("The total time taken:", endtime-begintime)
