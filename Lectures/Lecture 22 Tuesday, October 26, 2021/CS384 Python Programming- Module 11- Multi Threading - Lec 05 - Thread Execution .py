# from threading import *
import time
import threading

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
t1 = threading.Thread(target=divison, args=(numbers,))
t2 = threading.Thread(target=multiplication, args=(numbers,))
t1.start()
t2.start()

t1.join()
t2.join()

endtime = time.time()
print("The total time taken:", endtime-begintime)
