import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s',
                    )

def deamon():
    logging.debug('Starting...')
    time.sleep(10)
    logging.debug('End...')

d = threading.Thread(name='deamon', target=deamon())
d.setDaemon(True)

def non_deamon():
    logging.debug('Starting')
    logging.debug('Ending')

notD = threading.Thread(name = 'non-deamon', target = non_deamon)

d.start()
notD.start()
print('d is Alive', d.is_alive())