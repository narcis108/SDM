import threading

def afiseaza(i):
    print('functie apelata de thread-ul %i' % i)
    return

for i in range(5):
    thread = threading.Thread(target=afiseaza, args=(i,))
    thread.start()
    thread.join()
