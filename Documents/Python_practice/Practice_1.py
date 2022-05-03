import threading
import os

def one(x):
    print("Waiting 10 minutes to terminate", x)


def two(y):
    print("Waiting 5 minutes to terminate", y)


t1 = threading.Thread(target=one, args=5)
t2 = threading.Thread(target=two, args=2)
t2.start()
t2.join(5)
t1.start()
t1.join(10)

