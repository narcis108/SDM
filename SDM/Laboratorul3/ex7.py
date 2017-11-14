import threading, logging, time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s',
                    )


def worker(e):
    # asteapta sa se produca un eveniment
    logging.debug('asteapta evenimentul1')
    eveniment = e.wait()
    logging.debug('Se continuta procesarea...')


e = threading.Event()
w1 = threading.Thread(name='worker',
                      target=worker,
                      args=(e,))

w1.start()

logging.debug('Evenimentul va fi generat...')
time.sleep(3)
e.set()
logging.debug('Evenimentul a fost generat')
