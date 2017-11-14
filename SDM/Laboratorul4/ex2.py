import logging
import os
from threading import Thread
import sys
from timeit import Timer
from queue import Queue

import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s '
                    )

def build_directory_list(folder):
    list = []
    for (path, dir, files) in os.walk(folder):
        for file in files:
            list.append(os.path.join(path, file))
    return list

class threads_objects(Thread):
    def run(self):
        function_to_run(build_directory_list("C:\\Users\\GBS04655\\PycharmProjects"))


def thredead(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(consumer(queue))
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


class nothreads_objects(object):
    def run(self):
        function_to_run(build_directory_list("C:\\Users\\GBS04655\\PycharmProjects"))

def non_thredead(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_objects())
    for i in funcs:
        i.run()


def function_to_run(files):
    for file in files:
        print(file)


class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for file in build_directory_list("C:\\Users\\GBS04655\\PycharmProjects"):
                queue.put(file)
                logging.debug('added %s to queue' % (file))
                # time.sleep(3)

def show_results(func_name, results):
    print("%s %f seconds" % (func_name, results))


class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while(self.queue):
            item = self.queue.get()
            function_to_run(item)
            logging.debug('consumed %s item from the list' % (item))
            self.queue.task_done()


if __name__ == "__main__":
    repeat = 1
    number = 1
    queue = Queue()
    t1 = producer(queue)
    t1.start()

    num_threads = [1, 2, 4, 8, 32]
    print('Start...')
    for i in num_threads:
        t = Timer("non_thredead(%s)" % i, "from __main__ import non_thredead")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("non thredead (%s iters)" % i, best_result)
        t = Timer("thredead(%s)" % i, "from __main__ import thredead")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("thredead (%s threads)" % i, best_result)
    print('End...')
