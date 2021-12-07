
from threading import *
import os
os.system("cls")
print("Main thread name", current_thread().getName())

current_thread().setName("CS384_Thread")

print("After customise the thread name: ", current_thread().getName())
