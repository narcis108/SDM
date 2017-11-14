import threading
import time
from threading import Thread


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print('Start ' + self.name + "\n")
        print_time(self.name, self.delay, 5)
        print('End ' + self.name + "\n")

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s : %s" % (threadName, time.ctime(time.time())))
        counter -= 1

if __name__ == "__main__":
    thread1 = myThread(1, "thread1", 2)
    thread2 = myThread(2, "thread2", 1)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

