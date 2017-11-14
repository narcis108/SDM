import threading


class ScireText(threading.Thread):
    def __init__(self, toWrite, output, lock):
        threading.Thread.__init__(self)
        self.toWrite = toWrite
        self.output = output
        self.lock = lock

    def run(self):
        while self.toWrite:
            text = self.toWrite.pop()
            self.lock.acquire()
            sir = ''
            for i in range(1000):
                sir = str(i) + '  ' + str(text) + "\n"
                self.output.write(sir)
            print('Write done by %s' % self.name)
            self.lock.release()


if __name__ == '__main__':
    text1 = ['text1', 'text2']
    text2 = ['text3', 'text4']
    fisier = open('output.txt', 'w+')
    lock = threading.Lock()

    thread1 = ScireText(toWrite=text1, output=fisier, lock=lock)
    thread2 = ScireText(toWrite=text2, output=fisier, lock=lock)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    fisier.close()
