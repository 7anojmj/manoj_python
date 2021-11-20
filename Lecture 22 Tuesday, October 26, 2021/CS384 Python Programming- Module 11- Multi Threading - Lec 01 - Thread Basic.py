import threading
import os
os.system("cls")


def print_hi(num):
    print("Hi, you are customer ", num)
    print("Current Executing Thread: (print_hi)",
          threading.current_thread().getName())


print("Current Executing Thread (main):", threading.current_thread().getName())
print_hi(100)  # Non threading execution
t1 = threading.Thread(target=print_hi, args=(75,))  # creates a thread
t1.start()  # calls
t1.join()


print("End of Program")
