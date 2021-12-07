# Race in threads
import os
import threading
# global variable x
x = 0

os.system("cls")


def increment():
    """
    function to increment global variable x
    """
    global x
    x += 1


def thread_task():
    """
    task for thread
    calls increment function 100000 times.
    """
    for _ in range(100000):
        increment()


def main_task():
    global x
    # setting global variable x as 0
    x = 0

    # creating threads
    t1 = threading.Thread(target=thread_task)  # x++
    t2 = threading.Thread(target=thread_task)  # x++

    # start threads
    t1.start()

    t2.start()
    # wait until threads finish their job

    # t1.join()
    # t2.join()


if __name__ == "__main__":
    for i in range(10):
        main_task()
        print("Iteration {0}: x = {1}".format(i, x))
