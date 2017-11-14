import threading, time, logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s',
                    )

def worker1(e):
    logging.debug('worker1 Start')
    logging.debug('waiting for the other process to signal the flag')
    e.wait()
    logging.debug('got the flag')
    logging.debug('continuing')

e = threading.Event()
def worker2():
    logging.debug('entering worker2')
    logging.debug('doing some work')
    logging.debug('setting the Event flag')
    e.set()
    logging.debug('exiting worker2')

w1 = threading.Thread(name='worker1',
                      target=worker1,
                      args=(e,)
                      )
w2 = threading.Thread(name='worker2',
                      target=worker2
                      )

w1.start()
w2.start()