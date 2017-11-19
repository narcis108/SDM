import logging
from multiprocessing.pool import ThreadPool
from timeit import Timer

import common

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s '
                    )


def makePool_debug(num_threads):
    pool = ThreadPool(num_threads)
    results = pool.map(logging.debug, common.files)
    pool.close()
    pool.join()


def secvential_debug(files):
    for file in files:
        logging.debug(file)


if __name__ == "__main__":
    t = Timer("makePool_debug(%s)" % common.number_of_threads, "from __main__ import makePool_debug")
    result_thredead_debug = min(t.repeat(repeat=1, number=1))

    t = Timer("secvential_debug(%s)" % common.files, "from __main__ import secvential_debug")
    result_secvential_debug = min(t.repeat(repeat=1, number=1))

    print(common.show_results("thredead_debug(%s threads)" % common.number_of_threads, result_thredead_debug))
    print(common.show_results("secvential_debug() : ", result_secvential_debug))
