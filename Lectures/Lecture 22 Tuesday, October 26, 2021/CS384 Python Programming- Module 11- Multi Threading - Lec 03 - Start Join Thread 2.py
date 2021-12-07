# from threading import *

#start & join

import threading
import os
os.system("cls")


def display():
    for i in range(4):
        print("Child Thread")


t = threading.Thread(target=display)
t.start()
t.join()
for i in range(4):
    print("Main Thread")
