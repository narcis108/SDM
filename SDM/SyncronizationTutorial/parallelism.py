import logging
import os
from multiprocessing.dummy import Pool as ThreadPool
from timeit import Timer

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s '
                    )


def build_directory_list(folder):
    list = []
    for (path, dir, files) in os.walk(folder):
        for file in files:
            list.append(os.path.join(path, file))
    return list


files = build_directory_list("D:\EclipseWorkSpace")


def makePool(num_threads):
    # Make the Pool of workers
    pool = ThreadPool(num_threads)
    results = pool.map(logging.debug, files)
    pool.close()
    pool.join()


def show_results(func_type, best_result):
    print("%s %f seconds" % (func_type, best_result))


def sequential_run(files):
    for file in files:
        print(file)

if __name__ == "__main__":
    repeat = 1
    number = 1
    num_threads = [2]
    for i in num_threads:
        t = Timer("makePool(%s)" % i, "from __main__ import makePool")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("thredead(%s threads)" % i, best_result)

    t = Timer("sequential_run", "from __main__ import sequential_run")
    best_result = min(t.repeat(repeat=repeat, number=number))
    show_results("sequential() : ", best_result)