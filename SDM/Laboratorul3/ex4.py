import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s',
                    )
def worker1():
    logging.debug('Start...')
    time.sleep(6)
    logging.debug('End...')

def worker2():
    logging.debug('Start...')
    time.sleep(2)
    logging.debug('End...')

def worker3():
    logging.debug('Start...')
    time.sleep(4)
    logging.debug('End...')

w1 = threading.Thread(name = 'my_worker1', target=worker1)
w2 = threading.Thread(name = 'my_worker2', target=worker2)
w3 = threading.Thread(target=worker3)

w1.start()
w2.start()
w3.start()