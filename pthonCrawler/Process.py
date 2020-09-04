import multiprocessing
import time

# def process(index):
#     time.sleep(index)
#     print(f'Process: {index}')
#
# if __name__=='__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#     print(f'CPU number: {multiprocessing.cpu_count()}')
#     for p in multiprocessing.active_children():
#         print(f'Child process name: {p.name} id: {p.pid}')
#     print('Process Ended')

from multiprocessing import Process, Lock


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'Pid: {self.pid} LoopCount: {count}')


if __name__ == '__main__1':
    processes = []
    for i in range(2, 5):
        p = MyProcess(i)
        processes.append(p)
        p.daemon = True  # 守护进程
        p.start()
    for p in processes:
        p.join(10)  # 传参 1 代表超时时间

    print('Main Process ended')


def process():
    print('starting')
    time.sleep(5)
    print('finished')


if __name__ == '__main__2':
    p = multiprocessing.Process(target=process())
    print('Before:', p, p.is_alive())

    p.start()
    print('During:', p, p.is_alive())

    p.terminate()
    print('Terminate:', p, p.is_alive())

    p.join()
    print('Joined', p, p.is_alive())


# 进程互斥锁
class MyProcess(Process):
    def __init__(self, loop, lock):
        Process.__init__(self)
        self.loop = loop
        self.lock = lock

    def run(self):
        for count in range(self.loop):
            time.sleep(0.1)
            self.lock.acquire()
            print(f'Pid: {self.pid} LoopCount: {count}')
            self.lock.release()


if __name__ == '__main__3':
    lock = Lock()
    for i in range(10, 15):
        p = MyProcess(i, lock)
        p.start()



# 信号量
from multiprocessing import Semaphore, Queue
from random import random
buffer = Queue(10)
empty = Semaphore(2)
full = Semaphore(0)
lock = Lock()


class Consumer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            full.acquire()
            lock.acquire()
            num = buffer.get()
            print(print(f'Consumer get {num}'))
            time.sleep(1)
            lock.release()
            empty.release()


class Producer(Process):
    def run(self):
        global buffer, empty, full, lock
        while True:
            empty.acquire()
            lock.acquire()
            num = random()
            buffer.put(num)
            print(print(f'Producer put {num}'))
            time.sleep(1)
            lock.release()
            full.release()


if __name__ == '__main__4':
    p = Producer()
    c = Consumer()
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main process Ended')


# 管道
from multiprocessing import Pipe


class Consumer(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        self.pipe.send('Consumer Words')
        print(f'Consumer Received: {self.pipe.recv()}')


class Producer(Process):
    def __init__(self, pipe):
        Process.__init__(self)
        self.pipe = pipe

    def run(self):
        print(print(f'Producer Received: {self.pipe.recv()}'))
        self.pipe.send('Producer Words')


if __name__ == '__main__6':
    pipe = Pipe()
    p = Producer(pipe[0])
    c = Consumer(pipe[1])
    p.daemon = c.daemon = True
    p.start()
    c.start()
    p.join()
    c.join()
    print('Main Process Ended')


from multiprocessing import Pool


def function(index):
    print(f'Start process: {index}')
    time.sleep(3)
    print(f'End process {index}', )


if __name__ == '__main__7':
    pool = Pool(processes=3)
    for i in range(4):
        pool.apply_async(function, args=(i,))

    print('Main Process started')
    pool.close()
    pool.join()
    print('Main Process ended')



# 现在我们有一个 list，里面包含了很多 URL，另外我们也定义了一个方法用来抓取每个 URL 内容并解析，那么我们可以直接在 map 的第一个参数传入方法名，第 2 个参数传入 URL 数组。
import urllib.request
import urllib.error


def scrape(url):
    try:
        urllib.request.urlopen(url)
        print(f'URL {url} Scraped')
    except (urllib.error.HTTPError, urllib.error.URLError):
        print(f'URL {url} not Scraped')


if __name__ == '__main__':
    pool = Pool(processes=3)
    urls = [
        'https://www.baidu.com',
        'http://www.meituan.com/',
        'http://blog.csdn.net/',
        'http://xxxyxxx.net'
    ]
    pool.map(scrape, urls)
    pool.close()
