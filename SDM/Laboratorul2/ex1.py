import threading
import time

res1 = 0
res2 = 0
counter = 100000
my_lock = threading.Lock()


def increment_with_lock():
    global res1
    for i in range(counter):
        my_lock.acquire()
        res1 += 1
        my_lock.release()
    print('Increment result with lock: %s' % res1)


def decrement_with_lock():
    global res1
    for i in range(counter):
        my_lock.acquire()
        res1 -= 1
        my_lock.release()
    print('Decrement result with lock: %s' % res1)


def increment_without_lock():
    global res2
    for i in range(counter):
        res2 += 1
    print('Increment result without lock: %s' % res2)


def decrement_without_lock():
    global res2
    for i in range(counter):
        res2 -= 1
    print('Decrement result without lock: %s ' % res2)


if __name__ == "__main__":
    thread1 = threading.Thread(target=increment_with_lock)
    thread2 = threading.Thread(target=decrement_with_lock)
    thread3 = threading.Thread(target=increment_without_lock)
    thread4 = threading.Thread(target=decrement_without_lock)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print("res1: %s" % res1)
    print('res2: %s' % res2)
