from threading import Thread
import sys
from timeit import Timer


class threads_objects(Thread):
    def run(self):
        function_to_run()


def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(threads_objects())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


class nothreads_objects(object):
    def run(self):
        function_to_run()

def non_thredead():
    