import threading

class ScireText(threading.Thread):
    def __init__(self, toWrite, output):
        threading.Thread.__init__(self)
        self.toWrite = toWrite
        self.output = output

    def run(self):
        while self.toWrite:
            text = self.toWrite.pop()
            sir = ''
            for i in range(1000):
                sir = str(i) + '  ' + str(text) + "\n"
                self.output.write(sir)
            print('Write done by %s' %self.name)

if __name__ == '__main__':
    text1 = ['text1', 'text2']
    text2 = ['text3', 'text4']
    fisier = open('output.txt','w+')

    thread1 = ScireText(toWrite=text1,output= fisier)
    thread2 = ScireText(toWrite=text2, output=fisier)

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()