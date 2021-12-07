
import threading

import os
os.system("cls")


def m():
    print("Child Thread")
    print("Child Thread Identification Number:",
          threading.current_thread().ident)


t = threading.Thread(target=m)
t.start()
t.join()
print("Main Thread Identification Number:", threading.current_thread().ident)
print("Child Thread Identification Number:", t.ident)
