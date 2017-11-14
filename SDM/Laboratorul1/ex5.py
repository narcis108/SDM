import threading
import time

def afiseaza1():
    print('Start '+ threading.current_thread().getName()+"\n")
    time.sleep(2)
    print('End '+ threading.current_thread().getName()+"\n")
    return

def afiseaza2():
    print('Start '+ threading.current_thread().getName()+"\n")
    time.sleep(5)
    print('End '+ threading.current_thread().getName()+"\n")
    return

def afiseaza3():
    print('Start '+ threading.current_thread().getName()+"\n")
    time.sleep(3)
    print('End '+ threading.current_thread().getName()+"\n")
    return

if __name__=='__main__':
    thread1 = threading.Thread(name='thread1', target=afiseaza1)
    thread2 = threading.Thread(name='thread2', target=afiseaza2)
    thread3 = threading.Thread(name='thread3', target=afiseaza3)

    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

