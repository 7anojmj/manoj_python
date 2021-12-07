# https://dotnettutorials.net/lesson/multithreading-in-python/
import threading
import os
os.system("cls")


def print_hi(num):
    print("Hi, you are customer ", num)
    print("print_hi - Current Executing Thread:",
          threading.current_thread().getName())
    # infinite loop here...


def print_bye(num):
    print("Bye, you are customer ", num)
    print("print_bye - Current Executing Thread:",
          threading.current_thread().getName())


print("Current Executing Thread:", threading.current_thread().getName())

t1 = threading.Thread(target=print_hi, args=(75,))
t1.start()
t1.join()


t2 = threading.Thread(target=print_bye, args=(81,))
t2.start()
t2.join()

print("End")
