import threading
import time

class Box():
    lock = threading.RLock()
    def __init__(self):
        self.nr_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.nr_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()

def adder(box, items):
    while items>0:
        print('add 1 item to the box')
        box.add()
        items -= 1

def remover(box, items):
    while items > 0:
        print('remove 1 item from the box')
        box.remove()
        items -= 1

if __name__ == '__main__':
    items1 = 50
    box = Box()
    thread1 = threading.Thread(target=adder, args=(box, items1))
    thread2 = threading.Thread(target=remover, args=(box, items1))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

