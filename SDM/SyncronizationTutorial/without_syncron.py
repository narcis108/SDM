import threading
from urllib import request


class FetchURLs(threading.Thread):
    def __init__(self, urls, output):

        threading.Thread.__init__(self)
        self.urls = urls
        self.output = output

    def run(self):
        while self.urls:
            url = self.urls.pop()
            try:
                file = request.urlopen(url)
                self.output.write(file.read())
            except:
                print('Error opening the url')
            print('write done')


if __name__ == '__main__':
    f = open('output.txt', 'w+')
    # list 1 of urls to fetch
    urls1 = ['http://www.google.com', 'http://www.facebook.com']
    # list 2 of urls to fetch
    urls2 = ['http://www.yahoo.com', 'http://www.youtube.com']
    t1 = FetchURLs(urls1, f)
    t2 = FetchURLs(urls2, f)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    f.close()