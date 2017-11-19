from multiprocessing.dummy import Pool as ThreadPool
from timeit import Timer

import common


def makePool_print(num_threads):
    # Make the Pool of workers
    pool = ThreadPool(num_threads)
    results = pool.map(print, files)
    pool.close()
    pool.join()


def secvential_print(files):
    for file in files:
        print(file)


if __name__ == "__main__":
    repeat = 1
    number = 1
    number_of_threads = common.number_of_threads
    files = common.files

    t = Timer("makePool_print(%s)" % number_of_threads, "from __main__ import makePool_print")
    result_thredead_print = min(t.repeat(repeat=repeat, number=number))

    t = Timer("secvential_print(%s)" % files, "from __main__ import secvential_print")
    result_secvential_print = min(t.repeat(repeat=repeat, number=number))

    print(common.show_results("thredead_print(%s threads)" % number_of_threads, result_thredead_print))
    print(common.show_results("secvential_print() : ", result_secvential_print))
