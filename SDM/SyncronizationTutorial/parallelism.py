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


files = build_directory_list("H:\pycharm-edu-2.0.3")


def makePool(num_threads):
    # Make the Pool of workers
    pool = ThreadPool(num_threads)
    results = pool.map(print, files)
    pool.close()
    pool.join()


def show_results(func_type, best_result):
    result = "%s %f seconds" % (func_type, best_result)
    return result


def secvential(files):
    for file in files:
        print(file)


if __name__ == "__main__":
    repeat = 1
    number = 1
    num_threads = [8]
    for i in num_threads:
        t = Timer("makePool(%s)" % i, "from __main__ import makePool")
        best_result = min(t.repeat(repeat=repeat, number=number))
        result_thredead = show_results("thredead(%s threads)" % i, best_result)

    t = Timer("secvential(%s)" % files, "from __main__ import secvential")
    best_result = min(t.repeat(repeat=repeat, number=number))
    print('\n')
    print(show_results("secvential() : ", best_result))
    print(result_thredead)
