from multiprocessing.pool import ThreadPool
from timeit import Timer

import common


def makePool_count(num_threads):
    pool = ThreadPool(num_threads)
    results = pool.map(secvential_count, common.files)
    pool.close()
    pool.join()


def secvential_count(files):
    total = 0
    for _ in files:
        total += 1


if __name__ == "__main__":
    t = Timer("makePool_count(%s)" % common.number_of_threads, "from __main__ import makePool_count")
    result_thredead_count = min(t.repeat(repeat=1, number=1))

    t = Timer("secvential_count(%s)" % common.files, "from __main__ import secvential_count")
    result_secvential_count = min(t.repeat(repeat=1, number=1))

    print(common.show_results("thredead_count(%s threads)" % common.number_of_threads, result_thredead_count))
    print(common.show_results("secvential_count()",result_secvential_count))


