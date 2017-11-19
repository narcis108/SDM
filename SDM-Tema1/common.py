import os

def build_directory_list(folder):
    list = []
    for (path, dir, files) in os.walk(folder):
        for file in files:
            list.append(os.path.join(path, file))
    return list


def count_directories(folder):
    total = 0
    for file in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, file)):
            total += 1
    return total

def show_results(func_type, best_result):
    result = "%s %f seconds" % (func_type, best_result)
    return result

path = "C:\\"
files = build_directory_list(path)
number_of_threads = count_directories(path)
